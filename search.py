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
import os

from whoosh.fields import Schema, TEXT, KEYWORD, STORED, ID
from whoosh.index import create_in, open_dir, EmptyIndexError
from whoosh.qparser import QueryParser

INTRO_SCHEMA = Schema(
    resource_key=ID(stored=TRUE),
    name=TEXT(stored=True),
    keywords=KEYWORD(stored=True)
    content=TEXT)

INDEX_FILE_STORAGE = os.path.join(".", "index")

def main():
    pass

if __name__ == '__main__':
    main()
