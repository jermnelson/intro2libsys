import datetime
import json

def slugify():
    return ""

def add_person(info):
    info['@context'] = {'@vocab': 'http://schema.org/',
                        'bf': 'http://bibframe.org/vocab/'}
    info['bf:adminInfo'] = { 'bf:creationDate': datetime.datetime.utcnow().isoformat(),
                             "bf:descriptionConventions": "Using schema.org for descriptive metadata",
                             "bf:descriptionLanguage": "English"}

    if 'idloc:url' in info:
        info['@context']['idloc'] = "http://id.loc.gov"

    filename = slugify("{0} {1}".format(info.get('familyName'),
                                        info.get('givenName', '')))
    info['@id'] = 'http://intro2libsys.info/Person/{0}'.format(filename.strip())
    info['url'] = 'http://intro2libsys.info/Person/{0}{1}'.format(
        info.get('givenName'),
        info.get('familyName')).strip()

    with open("C:\\Users\\jernelson\\Development\\intro2libsys\\thing\\Person\\{0}.json".format(
        filename.strip()),
              'wb') as json_file:
        json.dump(info, json_file, indent=2, sort_keys=True)
    print("Finished adding {0}".format(filename))