from django.db import models

class Starship(models.Model):
    name = models.CharField(max_length=50)
    registry = models.CharField(max_length=11)
