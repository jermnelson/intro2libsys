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

app.register_blueprint(admin, prefix="admin")
app.register_blueprint(badges, prefix="badges")
app.register_blueprint(thing, prefix="thing")
app.register_blueprint(topics, prefix="topics")

toolbar = DebugToolbarExtension(app)

#app.config.from_envvar('APP_CONFIG_FILE')