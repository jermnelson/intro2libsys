"""
 `mod`:views Introduction to Library Systems Views
"""
__author__ = 'Jeremy Nelson'
from django.shortcuts import render_to_response
from django.template import RequestContext
from Curriculum.models import CourseSession
import datetime

def about(request):
    """
    About Introduction to Library Systems Distributed Learning System
    """
    return render_to_response('about.html',
                              {},
                              context_instance=RequestContext(request))

def home(request):
    """
    Default view for Introduction to Library Systems Course
    """
    sessions = CourseSession.objects.all()
    return render_to_response('index.html',
                             {'sessions':sessions,
                              'timestamp':datetime.datetime.today()},
                             context_instance=RequestContext(request))
