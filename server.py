__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'MIT'
__copyright__ = '(c) 2012-2014 by Jeremy Nelson'

import json
import os
from thing import get_article

from flask import Flask, g, jsonify, redirect, render_template

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_HOME = os.path.split(PROJECT_ROOT)[0]

app = Flask(__name__)

TOPIC_MAPS, TOPICS = [], {}
topic_maps_location = os.path.join(PROJECT_HOME,
                                   "intro2libsys",
                                   "topics",
                                   "topic-maps.json")
topic_maps = json.load(open(topic_maps_location))
topic_walker = os.walk(os.path.join(PROJECT_HOME,
                                    "intro2libsys",
                                    "topics"))
results = next(topic_walker)
for dir_name in results[1]:
    if not dir_name.startswith("template") and not dir_name.startswith("assets"):
        topic = json.load(open(os.path.join(PROJECT_HOME,
                                            "intro2libsys",
                                            "topics", 
                                            dir_name, 
                                            "{0}.json".format(dir_name))))
        TOPICS[dir_name] = topic
for topic_map in topic_maps.get('maps'):
    output = {'name': topic_map.get('jtm:name'), 'topics':[]}
    for topic_id in topic_map.get('jtm:topics'):
        output.get('topics').append(TOPICS[topic_id])
    TOPIC_MAPS.append(output)


@app.route("/<entity>/<name>.json")
def entity_json_view(entity,
              name):
    entity_filepath = os.path.join(PROJECT_ROOT,
                                    "thing",
                                    entity,
                                    "{0}.json".format(name))
    entity = json.load(open(entity_filepath))
    return jsonify(entity)

@app.route("/<entity>/<name>")
def entity_view(entity,
            name):
    ""
    entity_filepath = os.path.join(PROJECT_ROOT,
                                    "thing",
                                    entity,
                                    "{0}.json".format(name))
    if os.path.exists(entity_filepath):
        entity = json.load(open(entity_filepath))

        return render_template('entity.html',
                               entity=entity)

@app.route("/JeremyNelson/<md_page>.html")
def JeremyNelson(md_page):
    markdown = None
    with open(os.path.join('static',
                            'md',
                            '{0}.md'.format(md_page))) as raw_md:
        markdown = raw_md.read()
    return render_template('markdown.html',
                           markdown=markdown)

@app.route('/topics')
def topics():
    return render_template('topics.html',
                           page='topics',
                           topics={})

@app.route("/topics/<topic>")
def display_topic(topic):
    "Individual topic view"
    if not topic in TOPICS:
        return "{0} not found".format(topic)
    return render_template('topic.html',
                           topic=TOPICS.get(topic))

@app.route('/<entity>s')
def entity_listing(entity):
    entity_folderpath = os.path.join(PROJECT_ROOT,
                                     "thing",
                                     entity)
    entities = []
    if os.path.exists(entity_folderpath):
        results = next(os.walk(entity_folderpath))
        for filename in results[2]:
            if not filename.endswith("json"):
                continue
            filepath = os.path.join(PROJECT_ROOT,
                                    'thing',
                                    entity,
                                    filename)
            entities.append(json.load(open(filepath)))
    return render_template('entity-listing.html',
                           entity=entity,
                           entities=entities)

@app.route('/<page>')
def page_router(page):
    return render_template('{0}.html'.format(page),
                           page=page)

@app.route('/')
def index():
    return render_template('index.html',
                           topics=TOPICS)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    app.run(host=host,
            port=port,
            debug=True)
