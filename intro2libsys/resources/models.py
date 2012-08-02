from django.db import models

# Create your models here.

class Book(models.Model):
    rdaCreator = models.ForeignKey('Creator')
    rdaCopyrightDate = models.DateField(blank=True,null=True)
    rdaPreferredTitle = models.CharField(max_length=255)
    url = models.UrlField(blank=True,null=True)

class Creator(models.Model):
    dob = models.DateField(blank=True,null=True)
    family = models.CharField(max_length=255)
    given = models.CharField(max_length=255,blank=True,null=True)
    middle = models.CharField(max_length=255,blank=True,null=True)

