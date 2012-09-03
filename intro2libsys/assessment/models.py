"""
 :mod:`models` Assessment Models
"""
__author__ = "Jeremy Nelson"
from django.db import models
from syllabus.models import ClassDate

class Exercise(models.Model):
    date_of = models.ForeignKey(ClassDate)
    value = models.CharField(max_length=45)

class Question(models.Model):
    category = models.CharField(max_length=2,
                                choices=[("bl","boolean"),
                                         ("es","essay"),
                                         ("mc","multiple choice"),
                                         ("sa","short answer")])


    question = models.CharField(max_length=200)
    test = models.ForeignKey('Test')
    
class Test(models.Model):
    category = models.CharField(max_length=2,
                                choices=[("fl","final"),
                                         ("mt","mid-term"),
                                         ("qz","weekly quiz")])
    date_of = models.ForeignKey(ClassDate)
    
   
