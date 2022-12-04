from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, render

from .forms import ScoreSelectForm
from .models import Score


def get_scores(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ScoreSelectForm(request.POST)
        if form.is_valid():
            scores_list = get_list_or_404(
                Score,
                date__range=[
                    form.cleaned_data["startdate"],
                    form.cleaned_data["enddate"],
                ],
            )
            user_list: dict[str, dict[str, Any]] = {}
            for score in scores_list:
                user = score.user.name
                if user in user_list:
                    user_list[user]["scores"].append(score.score)
                    user_list[user]["total"] += score.score
                else:
                    scores = {"scores": [score.score], "total": score.score}
                    user_list[user] = scores

            return render(request, "scores/show_scores.html", {"user_list": user_list})

    else:
        form = ScoreSelectForm()

    return render(request, "scores/get_scores.html", {"form": form})
