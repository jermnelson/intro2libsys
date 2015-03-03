from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from .admin import admin
from .badges import badges
from .home import app 
from .thing import thing
from .topics import topics

app.debug = True
app.config.from_object('config.default')
app.config.from_pyfile('config.py')

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(badges, url_prefix="/badges")
app.register_blueprint(thing, url_prefix="/thing")
app.register_blueprint(topics, url_prefix="/topics")

toolbar = DebugToolbarExtension(app)

#for rule in app.url_map.iter_rules():
#        if rule.endpoint != 'static':
#            print(rule)
#app.config.from_envvar('APP_CONFIG_FILE')