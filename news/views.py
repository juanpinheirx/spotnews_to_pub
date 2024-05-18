from django.http import Http404
from django.shortcuts import get_object_or_404, render
from news.models import News


# Create your views here.
def home(request):
    news = {"news_list": News.objects.all()}
    return render(request, "home.html", news)


def details(request, id):
    news = {"news": get_object_or_404(News, id=id)}
    return render(request, "news_details.html", news)
