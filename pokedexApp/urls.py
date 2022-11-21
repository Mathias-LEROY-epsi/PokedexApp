from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('team/create', create_team, name='create_team'),
    path('teams', teams, name='teams'),
    path('team/<id>', update_team, name='team'),
]
