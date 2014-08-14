__version_info__ = ('0', '1', '1')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'MIT'
__copyright__ = '(c) 2012-2014 by Jeremy Nelson'

import datetime
import json
import markdown
import os
import re
import redis
import sys

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
    return author.get('name')[0]['@value']

@app.template_filter('author_works')
def author_works(author_id):
    author_id = author_id.split("/")[-1]
    if not author_id in THINGS['Person'] or REDIS_DS is None:
        return
    all_work_keys = REDIS_DS.keys("{0}:*".format(author_id))
    totals = {}
    for row in all_work_keys:
        cw_type = row.split(":")[-1]
        totals[cw_type] = REDIS_DS.scard(row)
    return totals



@app.template_filter('copyright_year')
def copyright_year(thing_id):
    thing_key = thing_id.split("/")[-1]
    for key in THINGS.keys():
        if thing_key in THINGS[key]:
            if 'copyrightYear' in THINGS[key][thing_key]:
                return THINGS[key][thing_key].get('copyrightYear')
            # Tries date published, usually in YYYY-MM-DD
            elif 'datePublished' in THINGS[key][thing_key]:
                first_four = THINGS[key][thing_key]['datePublished'][0:4]
                try:
                    int(first_four)
                    return first_four
                except:
                    pass

@app.template_filter('expand_part')
def expand_part(part):
    part_id = part.split("/")[-1]
    for name in ['Periodical', 'PublicationIssue', 'PublicationVolume']:
        if part_id in THINGS[name]:
            return """<a href="{}">{}</a>""".format(part,
                THINGS[name][part_id].get('name'))
    return



@app.template_filter('organization_name')
def organization_name(org_id):
    """
    Template filter takes an organization ID and returns the organization's
    name.

    :param org_id: Organization's ID
    """
    org_id = org_id.split("/")[-1]
    if not org_id in THINGS['Organization']:
        return
    org = THINGS['Organization'][org_id]
    return org.get('name')[0]['@value']




@app.template_filter('local_url')
def local_url(absolute_url):
    result = urlparse.urlparse(absolute_url)
    return result.path

@app.route("/archive/fall-2012")
@app.route("/archive/textbook")
def textbook_archive():
    return """Original Textbook for <a href="/">Introduction to Library Systems</a>
is currently being migrated to <a href="http://www.gitbook.io/">GitBook</a>."""

# Business Model Canvases
@app.route("/business-model-canvas/<name>")
def bmc(name):
    json_path = os.path.join(PROJECT_ROOT,
                             "business-model-canvases",
                             "{}.json".format(name))
    if not os.path.exists(json_path):
        raise(404)
    return render_template('business-model-canvas.html',
                           org= json.load(open(json_path, 'r')),
                           comment_form = UserCommentsForm(),
                           topics=TOPICS)

# Catalog Pull Platform
@app.route("/catalog-pull-platform")
def catalog_pull_platform():
    return render_template('catalog-pull-platform.html',
                           comment_form = UserCommentsForm(),
                           topics=TOPICS)

@app.route('/semantic-server')
def semantic_server():
    return render_template('semantic-server.html',
                           comment_form = UserCommentsForm(),
                           topics=TOPICS)

# Special route handling for Person
@app.route("/Person/<name>")
def person_view(name):
    if not name in THINGS['Person']:
        abort(404)
    person_filepath = os.path.join(
        PROJECT_ROOT,
        "thing",
        "Person",
        "{0}.json".format(name))
    if not os.path.exists(person_filepath):
        abort(404)
    person = json.load(open(person_filepath))
    works = []
    for key in THINGS.keys():
        if not key.startswith('Person'):
            for entity_key in THINGS[key]:
                entity = THINGS[key][entity_key]
                if 'author' in entity:
                    if {"@id": person.get('@id')} in entity.get('author'):
                        works.append(entity)
                if 'creator' in entity:
                    if {"@id": person.get('@id')} in entity.get('creator'):
                        works.append(entity)
    return render_template('person.html',
                           comments=get_comments(
                               entity_id=person.get('@id')),
                           comment_form = UserCommentsForm(),
                           entity=person,
                           entity_class='Person',
                           topics=TOPICS,
                           works=works)


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

@app.route("/<entity>/<name>/UserComments/add",
           methods=['POST'])
def entity_comment_add(entity,
                       name):
    if not entity in THINGS or not name in THINGS[entity]:
        abort(404)
    entity = THINGS[entity][name]
    comment_time = datetime.datetime.strptime(
        request.form.get('commentTime'),
        "%Y-%m-%d %H:%M:%S")
    comment_file = os.path.join(
        PROJECT_ROOT,
        "thing",
        "UserInteraction",
        comment_time.strftime("%Y-%m-%d.json"))
    user_comment = {"@type": "UserComments",
                    "@context": {"@vocab": "http://schema.org/"},
                    "creator": [
                        {"@id": request.form.get('creator')}],
                    "commentText": [
                        {"@value": request.form.get('commentText')}],
                    "commentTime": [
                        {"@value": comment_time.isoformat()}],
                    "discusses": [
                        {"@id":  entity.get('@id')}]}
    if name in COMMENTS:
        COMMENTS[name].append(user_comment)
    else:
        COMMENTS[name] = [user_comment,]
    if os.path.exists(comment_file):
        comments = json.load(open(comment_file))
        comments.append(user_comment)
    else:
        comments =[user_comment,]
    json.dump(
        comments,
        open(comment_file, 'w'),
        indent=2,
        sort_keys=True)

    return jsonify({'result': True})

@app.route("/<entity>/<name>/UserComments")
def entity_comments_listing(entity, name):
    return "Entity {} {}".format(entity, name)


@app.route("/<entity>/<name>")
def entity_view(entity,
                name):
    ""
    entity_class = entity
    if not entity in THINGS or not name in THINGS[entity]:
        abort(404)
    entity_filepath = os.path.join(PROJECT_ROOT,
                                   "thing",
                                   entity,
                                   "{0}.json".format(name))
    if not os.path.exists(entity_filepath):
        abort(404)
    entity = json.load(open(entity_filepath))
    for i, person_id in enumerate(entity.get('author', [])):
        author_id = person_id['@id'].split("/")[-1]
        if not author_id in THINGS['Person']:
            entity['author'][i] = person_id
        else:
            entity['author'][i] = THINGS['Person'][author_id]
    return render_template('entity.html',
                           comments=COMMENTS.get(name, []),
                           comment_form = UserCommentsForm(),
                           entity=entity,
                           entity_class=entity_class,
                           topics=TOPICS)


@app.route("/JeremyNelson/<page>.html")
def JeremyNelson(page=None):
    if not page:
        return url_for('page_router', page='about')
    page_path = os.path.join(PROJECT_ROOT,
                            'static',
                            'md',
                            '{0}.md'.format(page))
    if os.path.exists(page_path):
        with open(page_path) as raw_md:
            raw_mrkdwn = raw_md.read()
        meta_mrkdwn = markdown.Markdown(extensions=['meta'])
        mrkdwn_html = meta_mrkdwn.convert(raw_mrkdwn)
        return render_template('markdown.html',
                                markdown=mrkdwn_html,
                                comment_form = UserCommentsForm(),
                                topics=TOPICS)
    else:
        abort(404)

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
                           comment_form = UserCommentsForm(),
                           content=mrkdwn_html,
                           page='topics',
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
    app.run(host=host,
            port=port,
            debug=True)
