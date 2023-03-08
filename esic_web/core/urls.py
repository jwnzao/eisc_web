from django.urls import path
from .views import home_page, articles_page, actualites_page, presentation_page


urlpatterns = [
    #path('home/', include('home.urls')),
    path("", home_page, name="home"),
    path("articles", articles_page, name="articles"),
    path("actualites", actualites_page, name="actualites"),
    path("presentation", presentation_page, name="presentation"),
]

