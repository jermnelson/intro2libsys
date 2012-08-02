from django.db import models

class ClassDate(models.Model):
    end = models.DateTimeField(blank=True,null=True)
    md5_key = models.CharField(max_length=32)
    start = models.DateTimeField()
