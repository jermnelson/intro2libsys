__author__ = "Jeremy Nelson"

import json
import markdown
import os

from thing import THINGS

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_HOME = os.path.split(PROJECT_ROOT)[0]

class Topic(object):

    def __init__(self, json_file):
        self.name, self.pages, self.resources = None, [], []
        if os.path.exists(json_file):
            entity_json = json.load(open(json_file))
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
                self.pages.append({'url': os.path.join(self.name,
                                                      page),
                                  'name': name})
            for i, resource in enumerate(entity_json.get('readings', [])):
                for key in THINGS.keys():
                    if resource in THINGS[key]:
                        self.resources.append(THINGS[key][resource])
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
