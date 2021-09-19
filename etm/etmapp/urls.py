
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('task', views.task, name='task'),
    path('team', views.team, name='team'),
    path('meet', views.meet, name='meet'),
    path('filter', views.filter, name='filter'),
]



