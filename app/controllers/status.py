from __future__ import absolute_import, unicode_literals

from flask import Blueprint, jsonify


status_route = Blueprint('status', __name__)

@status_route.route('/status')
def status():
    return jsonify({ 'status': 'OK' })