from django.urls import path

from .views import get_scores


urlpatterns = [
    # ...
    path("", get_scores, name="get-scores"),
]
