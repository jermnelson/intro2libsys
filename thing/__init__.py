import datetime
import json
import os
import re
import sys
import urllib2


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_HOME = os.path.split(PROJECT_ROOT)[0]


THINGS = { 'Article': {},
           'BlogPosting': {},
           'Book': {},
           'MediaObject': {},
           'Organization': {},
           'Person': {},
           'Periodical': {},
           'PeriodicalIssue': {},
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
                     "rb"))
        except:
            print(name, sys.exc_info()[0])
        THINGS[key][name] = entity




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
    filename = slugify(info.get('headline'))
    if not '@type' in info:
        info['@type'] = 'Article'
    info['@id'] = urllib2.urlparse.urljoin(
        'http://intro2libsys.info',
        'Article/{0}'.format(filename))
    with open(os.path.join(file_location,
                           "Article",
                           "{0}.json".format(filename)),
              'wb') as json_file:
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
    filename = slugify(info.get('headline'))
    if not '@type' in info:
        info['@type'] = 'Book'
    info['@id'] = urllib2.urlparse.urljoin(
        'http://intro2libsys.info',
        'Book/{0}'.format(filename))
    with open(os.path.join(file_location,
                           "Book",
                           "{0}.json".format(filename)),
              'wb') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))


def add_blog_posting(info,
                     file_location=PROJECT_HOME):
    info = add_entity(info)
    filename = slugify(info.get('headline'))
    info['@id'] = urllib2.urlparse.urljoin(
        'http://intro2libsys.info',
        'BlogPosting/{0}'.format(filename))
    with open(os.path.join(file_location,
                           'BlogPosting',
                           '{0}.json'.format(filename)),
              'wb') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))





def add_entity(info,
               file_location=PROJECT_HOME):
    info['@context'] = get_context()
    info['bf:adminInfo'] = generate_adminInfo()
    return info

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

def add_periodical(info,
                   file_location=PROJECT_HOME):
    """
    Function adds a proposed schema.org/Periodical to intro2libsys collection.
    See http://www.w3.org/community/schemabibex/wiki/Periodical for more info.

    :param info: Dictionary of schema.org properties for the periodical
    :param file_location: Location of the thing directory, defaults to
                          PROJECT_ROOT
    """
    info['@context'] = get_context()
    info['bf:adminInfo'] = generate_adminInfo()
    if not '@type' in info:
        info['@type'] = 'Periodical'
    filename = slugify(info.get('name'))
    info['@id'] = urllib2.urlparse.urljoin(
        'http://intro2libsys.info',
        'Periodical/{0}'.format(filename))
    with open(os.path.join(file_location,
                           'Periodical',
                           '{0}.json'.format(filename)),
              'wb') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))

def add_periodical_issue(info,
                         file_location=PROJECT_HOME):
    """
    Function adds a proposed schema.org/Periodical to intro2libsys collection.
    See http://www.w3.org/community/schemabibex/wiki/Periodical#Thing_.3E_CreativeWork_.3E_Periodical
    for more info.

    :param info: Dictionary of schema.org properties for the PeriodicalIssue
    :param file_location: Location of the thing directory, defaults to
                          PROJECT_ROOT
    """
    info['@context'] = get_context()
    info['bf:adminInfo'] = generate_adminInfo()
    if not '@type' in info:
        info['@type'] = 'PeriodicalIssue'
    filename = slugify(info.get('name'))
    info['@id'] = urllib2.urlparse.urljoin(
        'http://intro2libsys.info',
        'PeriodicalIssue/{0}'.format(filename))
    with open(os.path.join(file_location,
                           'PeriodicalIssue',
                           '{0}.json'.format(filename)),
              'wb') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(info.get('@id')))


def add_person(info,
               file_location=PROJECT_HOME):
    info['@context'] = get_context()
    info['bf:adminInfo'] = generate_adminInfo()
    if 'idloc:url' in info:
        info['@context']['idloc'] = "http://id.loc.gov"
    filename = slugify(u"{0} {1}".format(info.get('familyName'),
                                        info.get('givenName', '')))
    info['@id'] = 'http://intro2libsys.info/Person/{0}'.format(filename.strip())
    info['url'] = u'http://intro2libsys.info/Person/{0}{1}'.format(
        info.get('givenName'),
        info.get('familyName')).strip()
    if not 'name' in info:
        info['name'] = u"{0} {1}".format(info.get('givenName', ''),
                                        info.get('familyName'))
    with open(os.path.join(file_location,
                           "Person",
                           "{0}.json".format(
                           filename.strip())),
              'wb') as json_file:
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
