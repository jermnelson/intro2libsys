"""
 :mod:`models` Assessment Models
"""
__author__ = "Jeremy Nelson"
from django.db import models
from syllabus.models import ClassDate

class Question(models.Model):
    question = models.CharField(max_length=200)
    test = models.ForeignKey('Test')
    type_of = models.CharField(max_length=2,
                               choices=[("bl","boolean"),
                                        ("es","essay"),
                                        ("mc","multiple choice"),
                                        ("sa","short answer")])

class Test(models.Model):
    date_of = models.ForeignKey(ClassDate)
    type_of = models.CharField(max_length=2,
                               choices=[("fl","final"),
                                        ("mt","mid-term"),
                                        ("qz","quiz")])
     
   
