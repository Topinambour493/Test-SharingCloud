from django.db import models


class Ressource(models.Model):
    label = models.CharField(max_length=40)
    localization = models.CharField(max_length=150, verbose_name="localisation")
    type = models.CharField(max_length=40)
    people_capacity = models.IntegerField(default=1, verbose_name="capacité") #il faudrait pouvoir bloquer les nombres inférieures à 1


    def __str__(self):
        return self.type
