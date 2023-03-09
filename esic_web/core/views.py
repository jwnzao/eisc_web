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

def formations(request):
    return render(request, "core/formations.html")

def temoignages(request):
    return render(request, "core/temoignages.html")

def evenements(request):
    return render(request, "core/evenements.html")

def dates(request):
    return render(request, "core/dates.html")


