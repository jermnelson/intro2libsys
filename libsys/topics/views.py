__author__ = "Jeremy Nelson"
__license__ = "MIT"

import markdown
import os
from . import topics, PROJECT_ROOT, TOPICS, TOPIC_MAPS
from .forms import UserCommentsForm

from flask import abort, render_template

@topics.route('/topics')
def all_topics():
    return render_template('topics.html',
                           comment_form = UserCommentsForm(),
                           page='topics',
                           topics=TOPICS,
                           topic_maps=TOPIC_MAPS)

@topics.route("/topics/<topic>")
def display_topic(topic):
    "Individual topic view"
    if not topic in TOPICS:
        abort(404)
    return render_template('topic-detail.html',
                           comment_form = UserCommentsForm(),
                           page='topics',
                           topic=TOPICS.get(topic),
                           topics=TOPICS)

@topics.route("/topics/<topic>/<page>")
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