"""
 :mod:`models` Learner Models for Intro2Libsys DSL
"""
__author__ = "Jeremy Nelson"
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from syllabus.models import ClassDate
from assessment.models import Test

class Attendance(models.Model):
    absent = models.BooleanField()
    date_of = models.OneToOneField(ClassDate)
    learner = models.OneToOneField('Learner')
    

class Learner(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    institution_email = models.EmailField(null=True,blank=True)
    user = models.OneToOneField(User)
    
class ProjectLog(models.Model):
    comments = models.TextField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    learner = models.OneToOneField(Learner)

class TestLog(models.Model):
    comments = models.TextField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    learner = models.OneToOneField(Learner)
    score = models.DecimalField(max_digits=5,decimal_places=2)
    test = models.OneToOneField(Test)


