__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'MIT'
__copyright__ = '(c) 2012-2014 by Jeremy Nelson'

import json
import markdown
import os
import urllib2
from thing import get_article, THINGS
from topics import TOPICS
from flask import abort, Flask, g, jsonify, redirect, render_template

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_HOME = os.path.split(PROJECT_ROOT)[0]

app = Flask(__name__)

TOPIC_MAPS = []
topic_maps_location = os.path.join(PROJECT_HOME,
                                   "intro2libsys",
                                   "topics",
                                   "topic-maps.json")
topic_maps = json.load(open(topic_maps_location))

for topic_map in topic_maps.get('maps'):
    output = {'name': topic_map.get('jtm:name'), 'topics':[]}
    for topic_id in topic_map.get('jtm:topics'):
        output.get('topics').append(TOPICS[topic_id])
    TOPIC_MAPS.append(output)

@app.template_filter('author_name')
def author_name(author_id):
    author_id = author_id.split("/")[-1]
    if not author_id in THINGS['Person']:
        return
    author = THINGS['Person'][author_id]
    return author.get('name')

@app.template_filter('local_url')
def local_url(absolute_url):
    result = urllib2.urlparse.urlparse(absolute_url)
    return result.path


@app.route("/<entity>/<name>.json")
def entity_json_view(entity,
              name):
    if not entity in THINGS or not name in THINGS[entity]:
        abort(404)
    entity = THINGS[entity][name]
    return jsonify(entity)

@app.route("/<entity>/<name>")
def entity_view(entity,
                name):
    ""
    if not entity in THINGS or not name in THINGS[entity]:
        abort(404)
    entity = THINGS[entity][name]
    for i, person_id in enumerate(entity.get('author')):
        author_id = person_id['@id'].split("/")[-1]
        if not author_id in THINGS['Person']:
            entity['author'][i] = person_id
        else:
            entity['author'][i] = THINGS['Person'][author_id]
    return render_template('entity.html',
                           entity=entity,
                           topics=TOPICS)

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
                           topics=TOPICS)

@app.route("/topics/<topic>")
def display_topic(topic):
    "Individual topic view"
    if not topic in TOPICS:
        return "{0} not found".format(topic)
    return render_template('topic-detail.html',
                           page='topics',
                           topic=TOPICS.get(topic),
                           topics=TOPICS)

@app.route("/topics/<topic>/<page>")
def display_page(topic, page):
    if not topic in TOPICS:
        abort(404)
    file_path = os.path.join(PROJECT_ROOT,
                             "topics",
                             topic,
                             "{0}.md".format(page))
    if not os.path.exists(file_path):
        abort(404)
    meta_mrkdwn = markdown.Markdown(extensions=['meta'])
    raw_mrkdwn = open(file_path, 'rb').read()
    mrkdwn_html = meta_mrkdwn.convert(raw_mrkdwn)
    return render_template('topic-page.html',
                           content=mrkdwn_html,
                           page='topics',
                           topics=TOPICS)
                           

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
                           entities=entities,
                           topics=TOPICS)

@app.route('/<page>')
def page_router(page):
    return render_template('{0}.html'.format(page),
                           page=page,
                           topics=TOPICS)

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
