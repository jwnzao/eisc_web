from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, "core/index.html")

def articles_page(request):
    return render(request, "core/articles.html")

def actualites_page(request):
    return render(request, "core/actualites.html")

def presentation_page(request):
    return render(request, "core/presentation.html")

