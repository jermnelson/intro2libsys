import datetime
from flask_wtf import Form
from wtforms import DateTimeField, SelectField, TextField, TextAreaField
from wtforms.validators import DataRequired, Length

class UserCommentsForm(Form):
    commentTime = DateTimeField(default=datetime.datetime.utcnow())
    commentText = TextAreaField()
    creator = TextField(default='anonymous')
    discusses = TextField()
    
    


def add_comment(**kwargs):
    """
    Adds a comment to the REDIS datastore

    :keyword redis_ds: Redis datastore, default is REDIS_DS
    """
    redis_ds = kwargs.get('redis_ds', REDIS_DS)
    redis_id = redis_ds.incr("global schema:UserComments")
    comment_key = "schema:UserComments:{0}".format(redis_id)
    commentTime = kwargs.get('commentTime',
                             datetime.datetime.utcnow())
    redis_ds.hset(comment_key,
                  'commentTime',
                  commentTime.isoformat())
    redis_ds.hset(comment_key,
                  'commentText',
                  kwargs.get('commentText',
                             ""))
    redis_ds.hset(comment_key,
                  'creator',
                  kwargs.get('creator', ['anonymous']))
    redis_ds.hset(comment_key,
                  'discusses',
                  kwargs.get('discusses',
                             'http://intro2libsys.info'))
    redis_ds.sadd('schema:UserComments:{0}'.format(
        kwargs.get('discusses', 'http://intro2libsys.info')),
        comment_key)
    redis_ds.setbit(commentTime.strftime("%Y-%m-%d:schema:UserComments"),
                    int(redis_id),
                    1)
    redis_ds.setbit(commentTime.strftime("%Y-%m:schema:UserComments"),
                    int(redis_id),
                    1)
    redis_ds.setbit(commentTime.strftime("%Y:schema:UserComments"),
                    int(redis_id),
                    1)
    redis_ds.save()


def get_comments(**kwargs):
    output = []
    redis_ds = kwargs.get('redis_ds', REDIS_DS)
    entity_id = kwargs.get('entity_id')
    if entity_id is not None:
        for row in redis_ds.smembers('schema:UserComments:{0}'.format(
            entity_id)):
            output.append(redis_ds.hgetall(row))
    return output
    
        
                      
