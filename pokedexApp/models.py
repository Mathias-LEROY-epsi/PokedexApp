from django.db import models


class TeamModel(models.Model):
    name = models.CharField(max_length=50)
    pokemon1 = models.CharField(max_length=50)
    pokemon2 = models.CharField(max_length=50)
    pokemon3 = models.CharField(max_length=50)
    pokemon4 = models.CharField(max_length=50)
    pokemon5 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
