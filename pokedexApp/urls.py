from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
=======
    path('team/create', views.create_team, name='create_team'),
    path('teams', views.teams, name='teams'),
    path('team/<id>', views.update_team, name='team'),

>>>>>>> 198fe06 (ajout creer, modifier, afficher Ãequipe)
]
