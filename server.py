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
    return render_template('index.html')


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    app.run(host=host,
            port=port,
            debug=True)
