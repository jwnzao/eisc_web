from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, "core/index.html")

def articles_page(request):
    return render(request, "core/articles.html")