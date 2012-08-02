"""
 `mod`:views Introduction to Library Systems Syllabus Views
"""
__author__ = 'Jeremy Nelson'
from django.shortcuts import render_to_response
from django.template import RequestContext
from syllabus.models import *
import datetime

def home(request):
    """
    Default view for Introduction to Library Systems Course
    """
    return render_to_response('syllabus.html',
                             {'timestamp':datetime.datetime.today()},
                              context_instance=RequestContext(request))

