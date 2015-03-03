__version_info__ = ('0', '1', '1')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'MIT'
__copyright__ = '(c) 2012-2015 by Jeremy Nelson and Intro2libsys.info LLC'

import datetime
import json
import markdown
import os
import re
import redis
import sys
print("BEFORE Any conditional processing")
try:
    import urllib2.urlparse as urlparse
except ImportError:
    import urllib.parse as urlparse

try:
    REDIS_DS = redis.StrictRedis(port=6380)
except:
    REDIS_DS = None

from collections import OrderedDict

from flask import abort, Flask, g, jsonify, redirect, render_template, request
from flask import url_for
from flask.ext.login import LoginManager, login_user, login_required, logout_user
from flask.ext.login import make_secure_token, UserMixin, current_user

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_HOME = os.path.split(PROJECT_ROOT)[0]

sys.path.append(os.path.join(PROJECT_HOME, 'intro2libsys'))
from search import Search
from user import Admin
from thing import get_article, COMMENTS, THINGS
from thing.UserInteraction import UserCommentsForm, add_comment, get_comments
from topics import TOPICS

app = Flask(__name__)
app.config.from_pyfile('intro2libsys.cfg')
login_manager = LoginManager()
login_manager.init_app(app)

FIRST_CHAR_RE = re.compile(r"[a-z]")

TOPIC_MAPS = []
topic_maps_location = os.path.join(PROJECT_HOME,
                                   "intro2libsys",
                                   "topics",
                                   "topic-maps.json")
print("Topic map location {}".format(topic_maps_location))
topic_maps = json.load(open(topic_maps_location))

for topic_map in topic_maps.get('maps'):
    output = {'name': topic_map.get('jtm:name'), 'topics':[]}
    for topic_id in topic_map.get('jtm:topics'):
        output.get('topics').append(TOPICS[topic_id])
    TOPIC_MAPS.append(output)










@app.template_filter('local_url')
def local_url(absolute_url):
    result = urlparse.urlparse(absolute_url)
    return result.path

@app.route("/archive/fall-2012")
@app.route("/archive/textbook")
def textbook_archive():
    return """Original Textbook for <a href="/">Introduction to Library Systems</a>
is currently being migrated to <a href="http://www.gitbook.io/">GitBook</a>."""



# Login
@app.route("/login",
           methods=["POST"])
def login():
    if request.method == 'POST':
        iri = request.POST.get('iri')
        raw_pwd = request.POST.get('pwd')

        login_user()





# Special route handling for Person


@app.route("/<entity>/<name>.json")
def entity_json_view(entity,
              name):
    if not entity in THINGS or not name in THINGS[entity]:
        abort(404)
    entity = THINGS[entity][name]
    return jsonify(entity)

##@app.route("/<entity>/<name>/UserComments")
##def entity_comments(entity,
##                    name)



@app.route("/<entity>/<name>/UserComments")
def entity_comments_listing(entity, name):
    return "Entity {} {}".format(entity, name)






@app.route('/topics')
def topics():
    return render_template('topics.html',
                           comment_form = UserCommentsForm(),
                           page='topics',
                           topics=TOPICS,
                           topic_maps=TOPIC_MAPS)

@app.route("/topics/<topic>")
def display_topic(topic):
    "Individual topic view"
    if not topic in TOPICS:
        abort(404)
    return render_template('topic-detail.html',
                           comment_form = UserCommentsForm(),
                           page='topics',
                           topic=TOPICS.get(topic),
                           topics=TOPICS)



first_char_re = re.compile(r"[a-z]")
@app.route('/<entity>s')
def entity_listing(entity):
    entity_folderpath = os.path.join(PROJECT_ROOT,
                                     "thing",
                                     entity)
    things = {}
    if os.path.exists(entity_folderpath):
        results = next(os.walk(entity_folderpath))
        total = 0
        for filename in results[2]:
            if not filename.endswith("json"):
                continue
            filepath = os.path.join(PROJECT_ROOT,
                                    'thing',
                                    entity,
                                    filename)
            entity_dict = json.load(open(filepath))

            if 'headline' in entity_dict:
                all_chars = entity_dict.get('headline')[0]['@value'].lower()

            elif 'name' in entity_dict:
                all_chars = entity_dict.get('name')[0]['@value'].lower()
            first_char = all_chars[0]
            if not FIRST_CHAR_RE.search(first_char):
                for char in all_chars:
                    if FIRST_CHAR_RE.search(char):
                        first_char = char
                        break
            if not first_char in things:
                things[first_char] = []
            things[first_char].append(entity_dict)
            total += 1
    sorted_things = OrderedDict()
    for key in sorted(things):
        sorted_things[key] = things.get(key)
    return render_template('entity-listing.html',
                           comment_form = UserCommentsForm(),
                           entity=entity,
                           entities=sorted_things,
                           topics=TOPICS,
                           total=total)

@app.route('/search',
           methods=['POST', 'GET'])
def search():
    if 'query' in request.args:
        query_phrase = request.args.get('query')
    elif 'query' in request.form:
        query_phrase = request.form.get('query')
    else:
        query_phrase = ''
    if 'page' in request.args:
        page = request.args.get('page')
    elif 'page' in request.form:
        page = request.form.get('page')
    else:
        page = 1
    results = Search(query_phrase, page)
    return render_template('search.html',
                           comment_form = UserCommentsForm(),
                           query_phrase=query_phrase,
                           results=results,
                           topics=TOPICS)


@app.route('/<page>')
def page_router(page):
    return render_template('{0}.html'.format(page),
                           comment_form = UserCommentsForm(),
                           page=page,
                           topics=TOPICS)

@app.route('/')
def index():
    return render_template('index.html',
                           comment_form = UserCommentsForm(),
                           topics=TOPICS)



if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080 # Default
    port = 8081 # Debug
    print("Before running app")
    app.run(host=host,
            port=port,
            debug=True)
