"""
 Collection of misc. functions for assiting development of the 
 Intro2LibSys DLS and MOOC.

"""
__author__ = "Jeremy Nelson"

def add_author(given, family, birth=None, death=None, idloc=None):
    author = {'givenName':given,
              'familyName':family}
    if birth is not None:
        author['birthDate'] = birth
    if death is not None:
        author['deathDate'] = death
    if idloc is not None:
        author['idloc:uri'] = idloc
    return author

def creative_work(type_of=None):
    doc = {"@context": {"@vocab": "http://schema.org/",
                        "idloc": "http://id.loc.gov"}}
    if type_of is not None:
        doc['@type'] = type_of
    return doc

