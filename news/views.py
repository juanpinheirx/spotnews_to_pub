from django.http import Http404
from django.shortcuts import get_object_or_404, render
from news.models import News


# Create your views here.
def home(request):
    news = {"news_list": News.objects.all()}
    return render(request, "home.html", news)


def details(request, id):
    try:
        news = get_object_or_404(News, id=id)
        context = {"news": news}
        return render(request, "news_details.html", context)
    except Http404:
        return render(request, "404.html")
