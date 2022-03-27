from turtle import title
from django.db import models

class WoodBuildings(models.Model):
    namename = models.CharField(max_length=30)
    healf = models.IntegerField()
    avatar = models.ImageField(blank=True)
class Building(models.Model):
    namename = models.CharField(max_length=30)
    healf = models.IntegerField()
    avatar = models.ImageField(blank=True)
