from django.urls import include, path
from news.views import categories_form, details, home, news_form
from rest_framework import routers
from news.views import CategoryViewSet

router = routers.DefaultRouter()

router.register(r"categories", CategoryViewSet)


urlpatterns = [
    path("http://127.0.0.1:8000", home, name="home-page"),
    path("news/<int:id>/", details, name="news-details-page"),
    path("categories/", categories_form, name="categories-form"),
    path("news", news_form, name="news-form"),
    path("api/", include(router.urls)),
]
