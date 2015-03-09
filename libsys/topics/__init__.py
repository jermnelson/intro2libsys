__author__ = "Jeremy Nelson"

import json
import markdown
import os

#from thing import THINGS
from flask import Blueprint

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_HOME = os.path.split(PROJECT_ROOT)[0]

topic_blueprint = Blueprint(
    'topics', 
    __name__,
    template_folder='templates',
    static_folder="static")


class Topic(object):

    def __init__(self, json_file):
        self.name, self.pages, self.resources = None, [], []
        if os.path.exists(json_file):
            entity_json = json.load(open(json_file))
            setattr(self, '@id', entity_json.get('@id'))
            self.name = os.path.split(entity_json.get('@id'))[-1]
            for i, page in enumerate(entity_json.get('pages')):
                meta_mrkdwn = markdown.Markdown(extensions=['meta'])
                raw_mrkdwn = None
                with open(os.path.join(PROJECT_HOME,
                                       "topics",
                                       self.name,
                                       "{0}.md".format(page))) as mrkdwn_file:
                    raw_mrkdwn = mrkdwn_file.read()
                mrkdwn_html = meta_mrkdwn.convert(raw_mrkdwn)
                if hasattr(meta_mrkdwn, 'Meta'):
                    name = meta_mrkdwn.Meta.get('title')
                else:
                    name = page
                self.pages.append({'url': "{0}/{1}".format(self.name,
                                                           page),
                                  'name': name})
#            for i, resource in enumerate(entity_json.get('readings', [])):
#                for key in THINGS.keys():
#                    if resource in THINGS[key]:
#                        self.resources.append(THINGS[key][resource])
            self.headline = entity_json.get('name')


TOPICS = {}
topic_walker = os.walk(os.path.join(PROJECT_HOME,
                                    "topics"))
results = next(topic_walker)
for dir_name in results[1]:
    topic = Topic(os.path.join(PROJECT_HOME,
                               "topics",
                               dir_name,
                               "{0}.json".format(dir_name)))
    TOPICS[dir_name] = topic

TOPIC_MAPS = []
topic_maps_location = os.path.join(PROJECT_HOME,
                                   "topics",
                                   "topic-maps.json")
topic_maps = json.load(open(topic_maps_location))

for topic_map in topic_maps.get('maps'):
    output = {'name': topic_map.get('jtm:name'), 'topics':[]}
    for topic_id in topic_map.get('jtm:topics'):
        output.get('topics').append(TOPICS[topic_id])
    TOPIC_MAPS.append(output)

from .views import *
