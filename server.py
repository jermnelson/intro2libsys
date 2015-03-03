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













