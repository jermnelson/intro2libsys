__author__ = "Jeremy Nelson"
__license__ = "MIT"

import markdown
import os
from . import topic_blueprint, PROJECT_ROOT, TOPICS, TOPIC_MAPS

from flask import abort, render_template

@topic_blueprint.route("/<topic>")
def display_topic(topic):
    "Individual topic view"
    if not topic in TOPICS:
        abort(404)
    return render_template('topics/detail.html',
                         #  comment_form = UserCommentsForm(),
                           page='topics',
                           topic=TOPICS.get(topic),
                           topics=TOPICS)

@topic_blueprint.route("/<topic>/<page>")
def display_page(topic, page):
    topic_obj = TOPICS.get(topic)
    if not topic_obj:
        abort(404)
    file_path = os.path.join(PROJECT_ROOT,
                             topic,
                             "{0}.md".format(page))
    print("File path is {}".format(file_path)) 
    if not os.path.exists(file_path):
        abort(404)
    meta_mrkdwn = markdown.Markdown(extensions=['meta'])
    raw_mrkdwn = open(file_path).read()
    mrkdwn_html = meta_mrkdwn.convert(raw_mrkdwn)
    return render_template('topics/page.html',
                           content=mrkdwn_html,
                           page='topics',
                           topics=TOPICS)

@topic_blueprint.route("/")
def all_topic():
    return render_template('topics/index.html',
                           topics=TOPICS,
                           topic_maps=TOPIC_MAPS)

