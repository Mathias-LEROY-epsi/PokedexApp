from django.db import models

# Create your models here.
<<<<<<< HEAD
=======

class TeamModel(models.Model):
    name = models.CharField(max_length=50)
    pokemon1 = models.CharField(max_length=50)
    pokemon2 = models.CharField(max_length=50)
    pokemon3 = models.CharField(max_length=50)
    pokemon4 = models.CharField(max_length=50)
    pokemon5 = models.CharField(max_length=50)


    def __str__(self):
        return self.name
>>>>>>> 198fe06 (ajout creer, modifier, afficher Ãequipe)
