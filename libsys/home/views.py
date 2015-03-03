__author__ = "Jeremy Nelson"
__license__ = "MIT"

import json
import markdown
import os
from flask import abort, render_template, request, url_for
from . import app

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


# Business Model Canvases
@app.route("/business-model-canvas/<name>")
def bmc(name):
    json_path = os.path.join(PROJECT_ROOT,
                             "business-model-canvases",
                             "{}.json".format(name))
    if not os.path.exists(json_path):
        abort(404)
    return render_template('business-model-canvas.html',
                           org=json.load(open(json_path, 'r')))

# Catalog Pull Platform
@app.route("/catalog-pull-platform")
def catalog_pull_platform():
    return render_template('catalog-pull-platform.html')

# Jeremy Nelson    
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
                                markdown=mrkdwn_html)
    else:
        abort(404)
    
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
    results = {'page': page}#Search(query_phrase, page)
    return render_template('search.html',
                           query_phrase=query_phrase,
                           results=results)

# Semantic Server
@app.route('/semantic-server')
def semantic_server():
    return render_template('semantic-server.html')

# Page Router    
@app.route('/<page>')
def page_router(page):
    return render_template('{0}.html'.format(page),
                           page=page)

# Index
@app.route('/')
def index():
    return render_template('index.html')