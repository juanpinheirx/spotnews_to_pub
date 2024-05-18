from django.urls import path
from news.views import home


urlpatterns = [
    path("http://127.0.0.1:8000", home, name="home-page"),
]
