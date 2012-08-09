from django.db import models

class ClassDate(models.Model):
    end = models.DateTimeField(blank=True,null=True)
    md5_key = models.CharField(max_length=32)
    start = models.DateTimeField()

class Reading(models.Model):
    class_date = models.ForeignKey(ClassDate)
    page_range = models.CharField(max_length=20,blank=True,null=True)
    title = models.CharField(max_length=120)
    url = models.URLField()

class TextbookChapter(models.Model):
    class_date = models.ForeignKey(ClassDate)
    title = models.CharField(max_length=120)
    url = models.URLField()
