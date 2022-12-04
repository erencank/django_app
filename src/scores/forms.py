from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import Score, User


class ScoreCreateForm(forms.ModelForm[Score]):
    class Meta:
        model = Score
        fields = "__all__"


class ScoreSelectForm(forms.Form):
    startdate = forms.DateField()
    enddate = forms.DateField()


# --------------------------------
# All this is basically because a new User Model is needed.
class UserCreateForm(forms.ModelForm[User]):

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ["name", "email", "birthday"]

    def clean_password2(self) -> str:
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "Password are not the same",
                code="password_mismatch",
            )
        return password2  # type: ignore[return-value]

    def _post_clean(self) -> None:
        super()._post_clean()  # type: ignore[misc]
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit: bool = True) -> User:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
