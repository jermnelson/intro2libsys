"""
  This module offers in-depth coverage of a single topic for Intro2Libsys 
"""
__author__ = "Jeremy Nelson"
import json
import markdown
import os
from intro.settings import PROJECT_HOME
from django.shortcuts import render
from django.template import Context, loader
from django.http import Http404, HttpResponse

TOPICS = {} 
topic_walker = os.walk(os.path.join(PROJECT_HOME, "topics"))
results = next(topic_walker)
for dir_name in results[1]:
    if not dir_name.startswith("template") and not dir_name.startswith("assets"):
        topic = json.load(open(os.path.join(PROJECT_HOME, 
                                            "topics", 
                                            dir_name, 
                                            "{0}.json".format(dir_name))))
        TOPICS[dir_name] = topic

def home(request):
    # Assumes all non-template and non-assets directories are special topics
    topic_order = sorted(TOPICS)
    topics = []
    for topic_key in topic_order:
        topics.append({topic_key:TOPICS.get(topic_key)})
    return render(request, 'topics.html', {'topics': topics})

def page(request, topic_name, page):
    page_path = os.path.join(PROJECT_HOME, 
                             "topics", 
                             topic_name, 
                             "{0}.md".format(page))
    if not os.path.exists(page_path):
        raise Http404
    topic = json.load(open(os.path.join(PROJECT_HOME,
                                        "topics",
                                         topic_name,
                                         "{0}.json".format(topic_name))))
    meta_md = markdown.Markdown(extensions=['meta'])
    raw_html = meta_md.convert(open(page_path, 'rb').read())
    if topic['pages'].index(page) == 0: # First Page in Topic
        previous_url = "/topics/{0}".format(topic_name)
    else:
        previous_url = "/topics/{0}/{1}".format(
            topic_name,
            topic['pages'][topic['pages'].index(page) - 1])
    if len(topic['pages']) - 1 == topic['pages'].index(page): # Last Page in Topic
        next_url = "/topics/{0}".format(topic_name)
    else:
        next_url = "/topics/{0}/{1}".format(
            topic_name,
            topic['pages'][topic['pages'].index(page) + 1])
        
    return render(request, 
                  'page.html', 
                  {'topic':topic,
                   'next': next_url,
                   'page':page,
                   'previous': previous_url,
                   'content':raw_html})
                                                               

def topic(request, name=None):
    topic_path = os.path.join(PROJECT_HOME, "topics", name)
    if os.path.exists(topic_path) and TOPICS.has_key(name):
        return render(request,
                      'topic-detail.html',
                      {'topic':TOPICS.get(name),
                       'key_name': name})
    else:
        raise Http404
