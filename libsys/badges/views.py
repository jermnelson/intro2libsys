"""
Blueprint for OpenBadge in Flask applications.

Copyright (c) 2014, 2015 Jeremy Nelson

"""

__version_info__ = ('0', '0', '5')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'MIT'
__copyright__ = '(c) 2014, 2015 by Jeremy Nelson'

import json

from flask import Blueprint, render_template, abort
from flask.views import View
from jinja2 import TemplateNotFound
from . import badges

class OpenBadgeView(View):

    def dispatch_request(self):
        return jsonify(self.output())

    
class BadgeClassInfo(OpenBadgeView):
    methods =['GET']

    def __init__(self):
        self.criteria = None
        self.description = None
        self.image = None
        self.issuer = None
        self.tags = []

    def output(self, name):
        return {"name": name,
                "description": self.description,
                "image": self.image,
                "criteria": self.criteria,
                "tags": self.tags,
                "issuer": self.issuer}

class BadgeIssuerOrg(OpenBadgeView):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.image = None
        self.url = None
        self.email = None
        self.revocationList = None

    def output(self):
        return {"name": self.name,
                "image": self.image,
                "url": self.url,
                "email": self.email,
                "revocationList": self.revocationList}

class IssueBadge(OpenBadgeView):

    def output(self):
        
        return {'message': self.message,
                'badge-url': self.assert_url}


badges.add_url_rule(
    "/<badge>/<name>", 
    view_func=BadgeClassInfo.as_view('badgeclassinfo'))

@badges.route("/")
def home():
    return render_template("badges/index.html")

