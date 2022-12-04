from django.contrib.auth.hashers import make_password
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create a model for Users with fields name, age,  email, password.
# This could probably be the built in Django User model. No need to seperate User model.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    birthday = models.DateField()

    @property
    def age(self) -> int:
        return int((timezone.now().date() - self.birthday).days / 365.25)

    def set_password(self, raw_password: str) -> None:
        self.password = make_password(raw_password)
        self._password = raw_password

    def __str__(self) -> str:
        return self.name


class Score(models.Model):
    user = models.ForeignKey(User, related_name="scores", on_delete=models.CASCADE)
    date = models.DateField(
        default=timezone.now,
    )  # Can also be a someting that the super admin fills in. Not specified which way.
    score = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],
    )

    def get_absolute_url(self) -> str:
        return reverse("scores-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.user.name}'s score"
