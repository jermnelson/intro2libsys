# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:32:19 2015

@author: Jeremy Nelson
"""
__author__ = "Jeremy Nelson"

import datetime
import json
import os
from flask import abort, jsonify, render_template
from . import thing, PROJECT_ROOT, THINGS

# Special route handling for Person
@thing.route("/Person/<name>")
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
                           comments=[],
                           entity=person,
                           entity_class='Person',
                           works=works)


@thing.route("/<entity>/<name>.json")
def entity_json_view(entity,
              name):
    if not entity in THINGS or not name in THINGS[entity]:
        abort(404)
    entity = THINGS[entity][name]
    return jsonify(entity)

##@app.route("/<entity>/<name>/UserComments")
##def entity_comments(entity,
##                    name)

@thing.route("/<entity>/<name>/UserComments/add",
           methods=['POST'])
def entity_comment_add(entity,
                       name):
    if not entity in THINGS or not name in THINGS[entity]:
        abort(404)
    if not app.debug:
        return jsonify({"result": False})
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

@thing.route("/<entity>/<name>/UserComments")
def entity_comments_listing(entity, name):
    return "Entity {} {}".format(entity, name)


@thing.route("/<entity>/<name>")
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
                           entity=entity,
                           entity_class=entity_class)