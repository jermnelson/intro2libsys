#-------------------------------------------------------------------------------
# Name:        search
# Purpose:     Provides full-text search for intro2libsys.info
#
# Author:      Jeremy Nelson
#
# Created:     2014-01-08
# Copyright:   (c) Jeremy Nelson 2014
# Licence:    MIT
#-------------------------------------------------------------------------------
__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'MIT'
__copyright__ = '(c) 2012-2014 by Jeremy Nelson'


import datetime
import json
import os

from whoosh.fields import Schema, TEXT, KEYWORD, STORED, ID
from whoosh.index import create_in, open_dir, EmptyIndexError
from whoosh.qparser import QueryParser

INTRO_SCHEMA = Schema(
    resource_key=ID(stored=True),
    name=TEXT(stored=True),
    creator=KEYWORD(stored=True),
    keywords=KEYWORD(stored=True),
    content=TEXT)



SITE_ROOT = os.path.abspath(os.path.dirname(__file__))

INDEX_FILE_STORAGE = os.path.join(SITE_ROOT, "index")

if os.path.exists(INDEX_FILE_STORAGE):
    try:
        INDEXER = open_dir(INDEX_FILE_STORAGE)
    except EmptyIndexError:
        INDEXER = create_in(INDEX_FILE_STORAGE,
                            INTRO_SCHEMA)
else:
    INDEXER = create_in(INDEX_FILE_STORAGE,
                        INTRO_SCHEMA)


def add_document(key,
                 name,
                 content,
                 creator=[],
                 keywords=[]):
    """
    Function takes an unique URI, a name, content, and optional list of keywords
    and adds to intro2libsys full-text search index.

    :param key: URI key of resource (usually in the format of
                http://intro2libys/{type}/{slugyfied-name}}
    :param name: Name or headline of the thing
    :param content: Full text of the article
    """
    ingestion_log = json.load(open(os.path.join(
        os.path.dirname(__file__),
        'log',
        'ingestion-log.json'),
        'rb'))
    writer = INDEXER.writer()
    writer.add_document(resource_key=key,
                        name=name,
                        content=content,
                        creator=u','.join(creator),
                        keywords=u','.join(keywords))
    writer.commit()
    ingested_on = datetime.datetime.utcnow()
    ingestion_event = {"agentType": "sof",
                       "eventRelatedObjectRole": {"out": key},
                       "eventType" : "ingestion",
                       "objectCategory": "representation",
                       "schema:description": "Index document {0} into Whoosh".format(name),
                       "schema:startDate": ingested_on.isoformat(),
                       "storageMedium": "har"}
    if ingested_on.strftime("%Y-%m-%d") in ingestion_log:
        ingestion_log[ingested_on.strftime("%Y-%m-%d")].append(ingestion_event)
    else:
        ingestion_log[ingested_on.strftime("%Y-%m-%d")] = [ingestion_event,]
    json.dump(ingestion_log,
              open(os.path.join(os.path.dirname(__file__),
                                'log',
                                'ingestion-log.json'), 'wb'),
              indent=2,
              sort_keys=True)


def Search(query_string,
           page=1):
    """
    Function takes a query_string and searches intro2libsys index

    :param query_string: Query string to search on
    :param page: Page of result set, defaults to 1
    """
    output = {'hits':[], 'page': int(page)}
    with INDEXER.searcher() as searcher:
        query = QueryParser("content", INTRO_SCHEMA).parse(query_string)
        results = searcher.search_page(query, int(page), pagelen=10)
        output['total'] = len(results)
        for i, hit in enumerate(results):
            fields = hit.fields()
            print(fields.get('creator'), fields.get('keywords'))
            output['hits'].append({'uri': fields.get('resource_key'),
                                   'name': fields.get('name'),
                                   'creator': fields.get('creator').split(",")})
    return output





def main():
    pass

if __name__ == '__main__':
    main()
