from django.db import models
from django.core import validators

class Ressource(models.Model):
    label = models.CharField(max_length=40)
    localization = models.CharField(max_length=150, verbose_name="localisation")
    type = models.CharField(max_length=40)
    people_capacity = models.IntegerField(default=1, verbose_name="capacité",validators=[validators.MinValueValidator(1)]) #cela bloque les nombres inférieurs à 1, uniquement lors des formulaires. 


    def __str__(self):
        return self.label
