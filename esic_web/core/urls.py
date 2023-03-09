from django.urls import path
from .views import home_page, articles_page, actualites_page, presentation_page, formations, dates, temoignages, evenements


urlpatterns = [
    # path('home/', include('home.urls')),
    path("", home_page, name="home"),
    path("articles", articles_page, name="articles"),
    path("actualites", actualites_page, name="actualites"),
    path("presentation", presentation_page, name="presentation"),
    path("formations", formations, name="formations"),
    path("dates", dates, name="dates"),
    path("temoignages", dates, name="temoignages"),
    path("evenements", dates, name="evenements"),
]
