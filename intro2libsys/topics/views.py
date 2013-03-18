"""
  This module offers in-depth coverage of a single topic for Intro2Libsys 
"""
__author__ = "Jeremy Nelson"
import os
from intro.settings import PROJECT_HOME
from django.views.generic.simple import direct_to_template
from django.http import Http404, HttpResponse

TOPICS = []
topic_walker = os.walk(os.path.join(PROJECT_HOME, "topics"))
results = next(topic_walker)
for dir_name in results[1]:
    if not dir_name.startswith("template") and not dir_name.startswith("assets"):
        TOPICS.append(dir_name)


def home(request):
    # Assumes all non-template and assets directories are special topics
    
    return direct_to_template(request,
                              'topics.html',
                              {'topics': TOPICS})

def topic(request, name=None):
    topic_path = os.path.join(PROJECT_HOME, "topics", name)
    if os.path.exists(topic_path):
        return HttpResponse("{0} topic detail".format(name))
    else:
        raise Http404
