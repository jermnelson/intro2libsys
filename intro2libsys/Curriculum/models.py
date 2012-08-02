"""
 :mod:`models` - 
"""
__author__ = 'Jeremy Nelson'

from django.db import models

class CourseSession(models.Model):
    """
    `CourseSession` models a discrete instructional block of time with
    continuous themes and expected outcomes.
    """
    end = models.DateTimeField(blank=True,null=True)
    label = models.CharField(max_length=150)
    md5_key = models.CharField(max_length=32)
    start = models.DateTimeField(blank=True,null=True)


class CourseOutcomes(models.Model):
    """
    `CourseOutcomes` associates a Curriculum Outcomes to a
    specific session.
    """
    label = models.CharField(max_length=255)
    session = models.ForeignKey(CourseSession)
    md5_key = models.CharField(max_length=32)
    redis_key = models.CharField(max_length=100,blank=True)
    
class CourseReadings(models.Model):
    """
    `CourseReadings` stores all readings used in a course
    """
    course_sessions = models.ManyToManyField(CourseSession,
                                             blank=True)
    end_reference = models.CharField(max_length=45,
                                     blank=True)
    label = models.CharField(max_length=255)
    md5_key = models.CharField(max_length=32)
    redis_key = models.CharField(max_length=100,blank=True)
    resource = models.ForeignKey('CourseResource',blank=True)
    start_reference = models.CharField(max_length=45,
                                       blank=True)
   
class CourseResource(models.Model):
    """
    `CourseResource` stores all resources used in a course.
    """
    course_sessions = models.ManyToManyField(CourseSession)
    label = models.CharField(max_length=150)
    md5_key = models.CharField(max_length=32)
 
 
    redis_key = models.CharField(max_length=100,blank=True)
    url = models.URLField(blank=True)

class CourseSlides(models.Model):
    """
    `CourseSlides` encapsulate a single view of a `CourseSession`
    """
    md5_key = models.CharField(max_length=32)
    
    next_slide = models.ForeignKey('self',
                                   null=True,
                                   blank=True)
    position = models.IntegerField(blank=True,null=True)
    session = models.ForeignKey(CourseSession)
    template = models.CharField(max_length=255)
    title = models.CharField(max_length=150)

class SlideContent(models.Model):
    """
    `SlideContent` contains either text or rst file location
    for slide content.
    """
    block_name = models.CharField(max_length=120)
    rstFile = models.CharField(max_length=255,
                               blank=True,
                               null=True)
    slide = models.ForeignKey(CourseSlides)
    text = models.TextField(blank=True,
                            null=True)
