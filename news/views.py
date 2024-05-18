from django.shortcuts import get_object_or_404, redirect, render
from news.forms import CreateCategoryForm, NewsForm
from news.models import Category, News, User
from rest_framework import viewsets
from news.serializers import CategorySerializer


# Create your views here.
def home(request):
    news = {"news_list": News.objects.all()}
    return render(request, "home.html", news)


def details(request, id):
    news = {"news": get_object_or_404(News, id=id)}
    return render(request, "news_details.html", news)


def categories_form(request):
    form = CreateCategoryForm()
    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {"form": form}
    return render(request, "categories_form.html", context)


def news_form(request):
    users = User.objects.all()
    categories = Category.objects.all()
    form = NewsForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home-page")

    return render(
        request,
        "news_form.html",
        {"form": form, "users": users, "categories": categories},
    )


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
