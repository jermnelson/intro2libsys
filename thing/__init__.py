import datetime
import json
import os
import re


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_HOME = os.path.split(PROJECT_ROOT)[0]


THINGS = { 'Article': [],
           'BlogPosting': [],
           'Book': [],
           'MediaObject': [],
           'Organization': [],
           'Person': [],
           'SoftwareApplication': [],
           'WebPage': []}


def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.
    """
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)

def add_entity(info,
               file_location=PROJECT_HOME):
    info['@context'] = get_context()
    info['bf:adminInfo'] = generate_adminInfo()
    return info


def add_person(info,
               file_location=PROJECT_HOME):
    info['@context'] = get_context()
    info['bf:adminInfo'] = generate_adminInfo()
    if 'idloc:url' in info:
        info['@context']['idloc'] = "http://id.loc.gov"
    filename = slugify("{0} {1}".format(info.get('familyName'),
                                        info.get('givenName', '')))
    info['@id'] = 'http://intro2libsys.info/Person/{0}'.format(filename.strip())
    info['url'] = 'http://intro2libsys.info/Person/{0}{1}'.format(
        info.get('givenName'),
        info.get('familyName')).strip()

    with open(os.path.join(file_location,
                           "Person",
                           "{0}.json".format(
                           filename.strip())),
              'wb') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info['@id']))

def add_organization(info,
                     file_location=PROJECT_HOME):
    info['@context'] = get_context()
    info['bf:adminInfo'] = generate_adminInfo()
    filename = slugify(info.get('name')).strip()
    if not '@type' in info:
        info['@type'] = 'Organization'
    info['@id'] = 'http://intro2libsys.info/Organization/{0}'.format(
                   filename)
    with open(os.path.join(file_location,
                           "Organization",
                           "{0}.json".format(filename)),
              "wb") as json_file:
        json.dump(info,
                  json_file,
                  indent=2,
                  sort_keys=True)
    print("Finished adding {0}.json".format(filename))


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
            'bf': 'http://bibframe.org/vocab/'}

def generate_adminInfo():
    return {'bf:creationDate': datetime.datetime.utcnow().isoformat(),
            "bf:descriptionConventions": "Using schema.org for descriptive metadata",
            "bf:descriptionLanguage": "English"}

def quick_dump(obj, category, id):
    json.dump(obj,
              open(os.path.join(PROJECT_HOME,
                                category,
                                '{0}.json'.format(id)),
                   'wb'),
              indent=2,
              sort_keys=True)
