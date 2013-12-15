__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'MIT'
__copyright__ = '(c) 2012-2014 by Jeremy Nelson'

import json
import os
from flask import Flask, g, jsonify, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    app.run(host=host,
            port=port,
            debug=True)
