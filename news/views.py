from django.shortcuts import get_object_or_404, redirect, render
from news.forms import CreateCategoryForm
from news.models import Category, News


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
