from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('home', views.logout_view, name="logout"),
    path('createcouncil', views.create_council, name="createcouncil"),
    path('events', views.events, name="events"),
    path('standings', views.standings, name="standings"),
    path('register/<event_id>', views.register, name="register"),
    path('inter_register', views.inter_register, name="inter_register"),
    path('hackathon', views.hackathon, name="hackathon"),
    path('mechathon', views.mechathon, name="mechathon"),
    path('valorant', views.valorant, name="valorant"),
    path('cod', views.cod, name="cod"),
    path('profile/<username>', views.profile, name="profile")
]