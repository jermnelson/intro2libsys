__author__ = "Jeremy Nelson"
__license__ = "MIT"

import datetime
import json
import os
import re
from collections import OrderedDict
from flask import abort, jsonify, render_template, request
from . import thing, COMMENTS, PROJECT_ROOT, THINGS

@thing.template_filter('author_name')
def author_name(author_id):
    author_id = author_id.split("/")[-1]
    if not author_id in THINGS['Person']:
        return
    author = THINGS['Person'][author_id]
    return author.get('name')[0]['@value']

@thing.template_filter('author_works')
def author_works(author_id):
    author_id = author_id.split("/")[-1]
    if not author_id in THINGS['Person']:
        return
    all_work_keys = REDIS_DS.keys("{0}:*".format(author_id))
    totals = {}
    for row in all_work_keys:
        cw_type = row.split(":")[-1]
        totals[cw_type] = REDIS_DS.scard(row)
    return totals



@thing.template_filter('copyright_year')
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

@thing.template_filter('expand_part')
def expand_part(part):
    part_id = part.split("/")[-1]
    for name in ['Periodical', 'PublicationIssue', 'PublicationVolume']:
        if part_id in THINGS[name]:
            return """<a href="{}">{}</a>""".format(part,
                THINGS[name][part_id].get('name'))
    return

@thing.template_filter('get_name')
def get_name(entity_id):
    entity_id = entity_id.split("/")[-1]
    for thing_type in THINGS.keys():
        if entity_id in THINGS[thing_type]:
            entity = THINGS[thing_type][entity_id]
            if 'name' in entity:
                return entity.get('name')[0]['@value']
            if 'headline' in entity:
                return entity.get('headline')[0]['@value']


@thing.template_filter('get_type')
def get_type(entity_id):
    entity_id = entity_id.split("/")[-1]
    for thing_type in THINGS.keys():
        if entity_id in THINGS[thing_type]:
            entity = THINGS[thing_type][entity_id]
            if type(entity['@type']) == list:
                return entity['@type'][0]['@value']
            else:
                return entity['@type']

@thing.template_filter('organization_name')
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

@thing.route("/<entity>/<name>/UserComments/add",
           methods=['POST'])
def entity_comment_add(entity,
                       name):
    if not entity in THINGS or not name in THINGS[entity]:
        abort(404)
    if not thing.debug:
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
                           

first_char_re = re.compile(r"[a-z]")
@thing.route('/<entity>s')
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
            if not first_char_re.search(first_char):
                for char in all_chars:
                    if first_char_re.search(char):
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
                           entity=entity,
                           entities=sorted_things,
                           total=total)