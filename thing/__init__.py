import datetime
import json
import os
import re
import sys


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_HOME = os.path.split(PROJECT_ROOT)[0]

COMMENTS = {}

walk_result = next(os.walk(
        os.path.join(
            PROJECT_HOME,
            "thing",
            "UserInteraction")))

for filename in walk_result[2]:
    if filename.endswith(".json"):
        daily_comment = json.load(open(os.path.join(
            PROJECT_HOME,
            "thing",
            "UserInteraction",
            filename)))
        for comment in daily_comment:
            for row in comment['discusses']:
                entity_id = row['@id'].split("/")[-1].split(".")[0]
                if entity_id in COMMENTS:
                    COMMENTS[entity_id].append(comment)
                else:
                    COMMENTS[entity_id] = [comment,]


THINGS = { 'Article': {},
           'BlogPosting': {},
           'Book': {},
           'DataCatalog': {},
           'Dataset': {},
           'MediaObject': {},
           'Organization': {},
           'Person': {},
           'Periodical': {},
           'Place': {},
           'PublicationIssue': {},
           'PublicationVolume': {},
           'SoftwareApplication': {},
           'WebPage': {}}

for key in THINGS.keys():
    result = next(os.walk(os.path.join(
        PROJECT_HOME,
        'thing',
        key)))
    for row in result[2]:
        name = row.split(".")[0]
        if len(name) < 1:
            continue
        try:
            entity = json.load(
                open(os.path.join(PROJECT_ROOT,
                                  key,
                                  row),
                     "r"))
            THINGS[key][name] = entity
        except:
            print(name, sys.exc_info()[0])






def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.
    """
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)

def add_article(info,
                file_location=PROJECT_HOME):
    info = add_entity(info)
    filename = slugify(info.get('headline')[0]['@value'])
    if not '@type' in info:
        info['@type'] = [{"@value": 'Article'}]
    info['@id'] = "/".join([
        'http://intro2libsys.info',
        'Article/{0}'.format(filename)])
    with open(os.path.join(file_location,
                           "Article",
                           "{0}.json".format(filename)),
              'w') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))

def add_book(info,
             file_location=PROJECT_ROOT):
    """
    Function adds a schema.org/Book to intro2libsys collection.

    :param info: Dictionary of schema.org properties for the book
    :param file_location: Location of the thing directory, defaults to
                          PROJECT_ROOT
    """
    info = add_entity(info)
    filename = slugify(info.get('headline')[0]['@value'])
    if not '@type' in info:
        info['@type'] = [{"@value": 'Book'}]
    info['@id'] = "/".join([
        'http://intro2libsys.info',
        'Book/{0}'.format(filename)])
    with open(os.path.join(file_location,
                           "Book",
                           "{0}.json".format(filename)),
              'w') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))


def add_blog_posting(info,
                     file_location=PROJECT_HOME):
    info = add_entity(info)
    filename = slugify(info.get('headline')[0]['@value'])
    if not '@type' in info:
        info['@type'] = [{"@value": 'BlogPosting'}]
    info['@id'] = "/".join([
        'http://intro2libsys.info',
        'BlogPosting/{0}'.format(filename)])
    with open(os.path.join(file_location,
                           'BlogPosting',
                           '{0}.json'.format(filename)),
              'w') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))




def add_entity(info,
               file_location=PROJECT_HOME):
    info['@context'] = get_context()
    info['mads:recordInfo'] = generate_adminInfo()
    return info

def add_organization(info,
                     file_location=PROJECT_HOME):
    info = add_entity(info)
    filename = slugify(info.get('name')[0]['@value']).strip()
    if not '@type' in info:
        info['@type'] = [{"@value": 'Organization'}]
    info['@id'] = 'http://intro2libsys.info/Organization/{0}'.format(
                   filename)
    with open(os.path.join(file_location,
                           "Organization",
                           "{0}.json".format(filename)),
              "w") as json_file:
        json.dump(info,
                  json_file,
                  indent=2,
                  sort_keys=True)
    print("Finished adding {0}.json".format(filename))

def add_periodical(info,
                   file_location=PROJECT_HOME):
    """
    Function adds a proposed schema.org/Periodical to intro2libsys collection.
    See http://www.w3.org/community/schemabibex/wiki/Periodical for more info.

    :param info: Dictionary of schema.org properties for the periodical
    :param file_location: Location of the thing directory, defaults to
                          PROJECT_ROOT
    """
    info=add_entity(info)
    if not '@type' in info:
        info['@type'] = [{"@value": 'Periodical'}]
    filename = slugify(info.get('name')[0]["@value"])
    info['@id'] = "/".join([
        'http://intro2libsys.info',
        'Periodical/{0}'.format(filename)])
    with open(os.path.join(file_location,
                           'Periodical',
                           '{0}.json'.format(filename)),
              'w') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))

def add_publication_issue(info,
                          file_location=PROJECT_HOME):
    """
    Function adds a proposed schema.org/PublicationIssue to intro2libsys collection.
    See http://www.w3.org/community/schemabibex/wiki/Article#New_Type:_PublicationVolume
    for more info.

    Args:
        info: Dictionary of schema.org properties for the PublicationIssue
        file_location: Location of the thing directory, defaults to
            PROJECT_ROOT
    """
    info=add_entity(info)
    if not '@type' in info:
        info['@type'] = [{"@value": 'PublicationIssue'}]
    filename = slugify(info.get('name')[0]["@value"])
    info['@id'] = "/".join([
        'http://intro2libsys.info',
        'PublicationIssue/{0}'.format(filename)])
    with open(os.path.join(file_location,
                           'PublicationIssue',
                           '{0}.json'.format(filename)),
              'w') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))


def add_place(info, file_location=os.path.join(PROJECT_HOME, 'Place')):
    info=add_entity(info)
    if not '@type' in info:
        info['@type'] = [{"@value":'Place'}]
    filename = slugify(info.get('name')[0]["@value"])
    info['@id'] = "/".join([
        'http://intro2libsys.info',
        'Place/{0}'.format(filename)])
    with open(os.path.join(file_location,
                           'Place',
                           '{0}.json'.format(filename)),
              'w') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))


def add_publication_volume(info,
                           file_location=PROJECT_HOME):
    """
    Function adds a proposed schema.org/PublicationVolume to intro2libsys collection.
    See http://www.w3.org/community/schemabibex/wiki/Article#New_Type:_PublicationVolume
    for more info.

    Args:
        info: Dictionary of schema.org properties for the PublicationVolume
        file_location: Location of the thing directory, defaults to
            PROJECT_ROOT
    """
    info=add_entity(info)
    if not '@type' in info:
        info['@type'] = [{"@value":'PublicationVolume'}]
    filename = slugify(info.get('name')[0]["@value"])
    info['@id'] = "/".join([
        'http://intro2libsys.info',
        'PublicationVolume/{0}'.format(filename)])
    with open(os.path.join(file_location,
                           'PublicationVolume',
                           '{0}.json'.format(filename)),
              'w') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))


def add_person(info,
               file_location=PROJECT_HOME):
    info=add_entity(info)
    if not '@type' in info:
        info['@type'] = [{"@value": 'Person'}]
    familyName = info['familyName'][0]['@value']
    if 'givenName' in info:
        givenName = info['givenName'][0]['@value']
        filename = "{} {}".format(familyName, givenName)
    else:
        filename = familyName
        givenName = ''
    filename = slugify(filename)
    info['@id'] = 'http://intro2libsys.info/Person/{0}'.format(filename.strip())
    info['url'] = [{"@value": info['@id']}]
    if not 'name' in info:
        info['name'] = [{"@value": "{} {}".format(givenName, familyName)}]
    with open(os.path.join(file_location,
                           "Person",
                           "{0}.json".format(
                           filename.strip())),
              'w+') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info['@id']))


def add_webpage(info,
                file_location=PROJECT_HOME):
    info=add_entity(info)
    filename = slugify(info.get('name')[0]["@value"])
    info['@id'] = 'http://intro2libsys.info/WebPage/{0}'.format(filename.strip())
    with open(os.path.join(file_location,
                           "WebPage",
                           "{0}.json".format(
                           filename.strip())),
              'w') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info['@id']))

def get_article(article_string):
    # Checks to see if article_string is a URI
    if article_string.startswith("http"):
        article_name = os.path.split(ariticle_string)[-1]
    else:
        article_name = article_string
    article_path = os.path.join(PROJECT_HOME,
                                "thing",
                                "Article",
                                "{0}.json".format(article_name))
    if os.path.exists(article_path):
        return json.load(open(article_name, 'rb'))

def get_context():
    return {'@vocab': 'http://schema.org/',
            'bf': 'http://bibframe.org/vocab/',
            'mads': 'http://www.loc.gov/standards/mads/'}

def generate_adminInfo():
    return {'mads:recordCreationDate': [{"@value": datetime.datetime.utcnow().isoformat()}],
            "mads:descriptionStandards": [{"@value":"Using schema.org for descriptive metadata"}],
            "mads:languageOfCataloging": [{"@value": "English"}]}



def quick_dump(obj, category, id):
    json.dump(obj,
              open(os.path.join(PROJECT_ROOT,
                                category,
                                '{0}.json'.format(id)),
                   'wb'),
              indent=2,
              sort_keys=True)

def update_entity(entity):
    if 'bf' in entity['@context']:
        entity['@context'].pop('bf')
    if 'loc' in entity['@context']:
        entity['@context'].pop('loc')
    if not 'mads' in entity['@context']:
        entity['@context']['mads'] = 'http://www.loc.gov/standards/mads/'
    if not 'mads:recordInfo' in entity:
        entity['mads:recordInfo'] = {
            'mads:descriptionStandards': [{"@value": ""}],
            'mads:languageOfCataloging': [{"@value": ""}],
            'mads:recordCreationDate': [{'@value': "" }],
            "mads:recordChangeDate": [
                {"@value": datetime.datetime.utcnow().isoformat()}]}
    else:
        for key in entity['mads:recordInfo'].keys():
            if key.startswith("loc:"):
                value = entity['mads:recordInfo'].pop(key)
                entity['mads:recordInfo'][key.replace("loc:", "mads:")] = \
                    [{"@value": value}]

    if 'bf:adminInfo' in entity:
        bf_adminInfo = entity.pop('bf:adminInfo')
        entity['mads:recordInfo']['mads:descriptionStandards'][0]['@value'] = \
            bf_adminInfo["bf:descriptionConventions"]
        entity['mads:recordInfo']['mads:languageOfCataloging'][0]['@value'] = \
            bf_adminInfo["bf:descriptionLanguage"]
        entity['mads:recordInfo']['mads:recordCreationDate'][0]['@value'] = \
            bf_adminInfo["bf:creationDate"]
    for key, value in entity.items():
        if key.startswith('author'):
            continue
        if not key.startswith("@") and not key.startswith("mads:"):
            if type(value) != list:
                entity[key] = [{"@value": value}]
            elif type(value) == dict:
                continue
            else:
                new_list = []
                for row in value:
                    new_list.append({"@value": row})
                entity[key] = new_list





