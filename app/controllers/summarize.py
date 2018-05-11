from __future__ import absolute_import, unicode_literals

from flask import Blueprint, jsonify, request
from models.cliff import Cliff

import json

summarize_route = Blueprint('summarize', __name__)

@summarize_route.route('/summarize', methods=['POST'])
def summarize():
    payload = json.loads(request.data)
    parser = Cliff()
    summary = parser.process(document=payload['data'])
    
    return jsonify({
        'data': {
            'lines': len(summary),
            'summary': summary
        }
    }), 200