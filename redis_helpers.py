#-------------------------------------------------------------------------------
# Name:        redis_helpers
# Purpose:     Redis Helpers for intro2libsys.info site
#
# Author:      Jeremy Nelson
#
# Created:     2014-01-21
# Copyright:   (c) Jeremy Nelson 2014
# Licence:     MIT
#-------------------------------------------------------------------------------

import redis
from thing import THINGS, slugify

def update_creative_works(name,
                          local_ds=redis.StrictRedis(port=6380)):
    for key in THINGS[name].keys():
        creative_work = THINGS[name].get(key)
        # Adds the thing URI to a hash look-up
        local_ds.hset('schema:{0}'.format(name),
                      creative_work.get('@id'),
                      key)
        # Adds the creative work key to a set for each type of creative work
        for row in creative_work.get('author', []):
            person_key = local_ds.hget('schema:Person',
                                       row.get('@id'))
            local_ds.sadd("{0}:{1}".format(person_key, name),
                          key)
        # Adds the creative work to the set for each year
        if 'copyrightYear' in creative_work:
            year_key ='{0}:copyrightYear'.format(creative_work.get('copyrightYear'))
            local_ds.sadd(year_key, key)
        # Adds creative_work key to set for each keyword that has been
        # lowercased
        if 'keywords' in creative_work:
            for keyword in creative_work.get('keywords'):
                local_ds.sadd('keyword:{0}'.format(slugify(keyword)),
                              key)







