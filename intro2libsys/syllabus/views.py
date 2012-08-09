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
    class_dates = ClassDate.objects.all().order_by('start')
    classes = []
    for date in class_dates:
        class_info = {'date':date}
        class_info['chapters'] = TextbookChapter.objects.filter(class_date=date.pk)
        classes.append(class_info)       
    return render_to_response('syllabus.html',
                             {'classes':classes,
                              'timestamp':datetime.datetime.today()},
                              context_instance=RequestContext(request))

