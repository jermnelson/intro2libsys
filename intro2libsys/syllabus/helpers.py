"""
 mod:`helpers` Module provides JSON and Redis helpers for Intro2LibSys syllabus 
"""
__author__ = "Jeremy Nelson"

import json

def add_author(filename):
    """
    Helper function prompts for author and saves back to filename
    """
    reading = json.load(open(filename,'rb'))
    new_author = {}
    print(reading.get('name'))
    if "author" in reading:
        print("An author already exists in reading. Continue?")
        continue_add_author = raw_input("(y)>>")
        if continue_add_author.lower() != 'y':
            return
        if type(reading.get('author')) is dict:
            print("Multiple authors, creating a list")
            first_author = reading.pop('author')
            reading['author'] = [first_author,]
    given = raw_input("given >>")
    if len(given) > 0:
        new_author['givenName'] = given.strip()
    family = raw_input("family >>")
    if len(family) > 0:
        new_author['familyName'] = family
    loc_prompt = raw_input("Has loc URI? (y)>>")
    if loc_prompt.lower() == 'y':
        idloc_uri = raw_input(" URI from id.loc.gov>>")
        if len(idloc_uri) > 0:
            new_author['idloc:uri'] = idloc_uri
    if "author" not in reading:
        reading['author'] = new_author
    else:
        reading['author'].append(new_author)
    json.dump(reading, open(filename, 'wb'), indent=2, sort_keys=True)

def keep_and_make_schema(filename):
    readings = json.load(open(filename, 'rb'))
    counter = 2
    for row in readings:
        title = row['fields']['title']
        keep_title = raw_input("Keep {0} >>(y|n)".format(title))
        if keep_title.lower() != 'y':
            continue
        counter += 1
        record = {"@context": {"@vocab":"http://schema.org/"},
                  "@id": "http://intro2libsys.info/resources/{0}".format(counter),
                  "name":title}
        if 'url' in row['fields']:
            record['url'] = row['fields']['url']
        json.dump(record,
                  open("C:\\Users\\jernelson\\Development\\intro2libsys\\intro2libsys\\syllabus\\fixures\\reading{0}.json".format(counter),"wb"),
                  indent=2,
                  sort_keys=True)
