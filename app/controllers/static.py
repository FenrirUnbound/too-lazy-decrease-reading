from __future__ import absolute_import, unicode_literals

from flask import Blueprint, send_from_directory


static_route = Blueprint('static', __name__)

@static_route.route('/')
def index():
    return send_from_directory('static', 'index.html')

@static_route.route('/static/js/<path:path>')
def javascript(path):
    return send_from_directory('static/js', path)

@static_route.route('/static/css/<path:path>')
def css(path):
    return send_from_directory('static/css', path)

@static_route.route('/static/media/<path:path>')
def media(path):
    return send_from_directory('static/media', path)
