# -*- coding: utf-8 -*-
"""
Blueprint for OpenBadge in Flask applications.

Created on Tue Mar  3 14:46:38 2015

Copyright (c) 2015 Jeremy Nelson

@author: Jeremy Nelson
"""
__author__ = "Jeremy Nelson"
__license__ = 'MIT'
__copyright__ = '(c) 2015 by Jeremy Nelson'

import json

from flask import Blueprint

badges = Blueprint('badges', 
                   __name__,
                   static_folder='static',
                   template_folder='templates')

from .views import *
