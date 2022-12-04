from django.contrib import admin

from .forms import ScoreCreateForm, UserCreateForm
from .models import Score, User


class ScoreAdmin(admin.ModelAdmin[Score]):
    list_display = ["user", "date", "score"]
    search_fields = ["user"]

    form = ScoreCreateForm


class UserAdmin(admin.ModelAdmin[User]):
    list_display = ["email"]
    search_fields = ["user", "email"]

    form = UserCreateForm


admin.site.register(Score, ScoreAdmin)
admin.site.register(User, UserAdmin)
