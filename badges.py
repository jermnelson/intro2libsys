"""
Blueprint for OpenBadge in Flask applications.

Copyright (c) 2014 Jeremy Nelson

"""

__version_info__ = ('0', '0', '5')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'MIT'
__copyright__ = '(c) 2014 by Jeremy Nelson'

import json

from flask import Blueprint, render_template, abort
from flask.views import View
from jinja2 import TemplateNotFound


class OpenBadgeView(View):

    def dispatch_request(self):
        return jsonify(self.output())

    
class BadgeClassInfo(OpenBadgeView):

    def output(self):
        return {"name": self.name,
                "description": self.description,
                "image": self.image,
                "criteria": self.criteria,
                "tags": self.tags,
                "issure": self.issuer}

class BadgeIssuerOrg(OpenBadgeView):

    def output(self):
        return {"name": self.name,
                "image": self.image,
                "url": self.url,
                "email": self.email,
                "revocationList": self.revocationList}

class IssueBadge(OpenBadgeView):

    def output(self):
        return {'message', self.message,
                'badge-url': self.assert_url}
