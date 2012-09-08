"""
 :mod:`models` - 
"""
__author__ = 'Jeremy Nelson'

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Instructor(models.Model):
    """
    Instructor model for Intro2LibSys course.
    """
    alt_email = models.EmailField(null=True,blank=True)
    profile_image_link = models.CharField(max_length=150,
                                          null=True,
                                          blank=True)
    user = models.OneToOneField(User)

