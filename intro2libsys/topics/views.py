"""
  This module offers in-depth coverage of a single topic for Intro2Libsys 
"""
__author__ = "Jeremy Nelson"
import markdown
import os
from intro.settings import PROJECT_HOME
from django.views.generic.simple import direct_to_template
from django.http import Http404, HttpResponse

TOPICS = []
PAGES = {}
topic_walker = os.walk(os.path.join(PROJECT_HOME, "topics"))
results = next(topic_walker)
for dir_name in results[1]:
    if not dir_name.startswith("template") and not dir_name.startswith("assets"):
        TOPICS.append(dir_name)
        if not PAGES.has_key(dir_name):
            PAGES[dir_name] = {}
        topic_file_walker = next(os.walk(os.path.join(PROJECT_HOME, "topics", dir_name)))
        for filename in topic_file_walker[2]:
            name, ext = os.path.splitext(filename)
            if ext == '.md':
                PAGES[dir_name][name] = filename

def home(request):
    # Assumes all non-template and assets directories are special topics
    
    return direct_to_template(request,
                              'topics.html',
                              {'topics': TOPICS})

def page(request, topic, page):
    page_path = os.path.join(PROJECT_HOME, "topics", topic, "{0}.md".format(page))
    if not os.path.exists(page_path):
        raise Http404
    meta_md = markdown.Markdown(extensions=['meta'])
    raw_html = meta_md.convert(open(page_path, 'rb').read())
    return direct_to_template(request,
                              'page.html',
                              {'topic':topic,
                               'page':page,
                               'content':raw_html})
                                 

def topic(request, name=None):
    print("In topic {0}".format(name))
    topic_path = os.path.join(PROJECT_HOME, "topics", name)
    if os.path.exists(topic_path):
        return HttpResponse("{0} topic detail".format(name))
    else:
        raise Http404
