__author__ = "Jeremy Nelson"

from django.db import models

class Chapter(models.Model):
    title = models.CharField(max_length=200)

class Page(models.Model):
    chapter = models.ForeignKey(Chapter)
    location = models.CharField(max_length=50)
    order = models.IntegerField()
    title = models.CharField(max_length=150,
                             blank=True)
                             
