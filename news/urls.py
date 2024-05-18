from django.urls import path
from news.views import details, home


urlpatterns = [
    path("http://127.0.0.1:8000", home, name="home-page"),
    path("news/<int:id>/", details, name="news-details-page"),
]
