from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


def formationDevelopper(request):
    return render(request, "core/formationDevelopper.html")


def businessEngineering(request):
    return render(request, "core/businessEngineering.html")


def dataScience(request):
    return render(request, "core/dataScience.html")


def cybersecurity(request):
    return render(request, "core/cybersecurity.html")


def certifications(request):
    return render(request, "core/certifications.html")


def temoignages(request):
    return render(request, "core/temoignages.html")


def evenements(request):
    return render(request, "core/evenements.html")


def dates(request):
    return render(request, "core/dates.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")

    context = {}
    return render(request, "core/login.html", context)


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:home")
        else:
            messages.error(request, "An error occured during registration")
    context = {"form": form}
    return render(request, "core/register.html", context)


def logout_page(request):
    logout(request)
    return redirect("home")
