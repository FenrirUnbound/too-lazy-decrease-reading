from __future__ import absolute_import, unicode_literals

from flask import Blueprint, jsonify, request
from models.cliff import Cliff

import json

DEFAULT_ALG = 'lsa'

summarize_route = Blueprint('summarize', __name__)

@summarize_route.route('/summarize', methods=['POST'])
def summarize():
    algorithm = request.args.get('alg')
    if algorithm is None or len(algorithm) == 0:
        algorithm = DEFAULT_ALG

    payload = json.loads(request.data)
    parser = Cliff()
    summary = []

    try:
        summary = parser.process(document=payload['data'], algorithm=algorithm)
    except KeyError:
        return jsonify({
            'error': 'Unknown summary algorithm: {0}'.format(algorithm)
        }), 400
    
    return jsonify({
        'data': {
            'lines': len(summary),
            'summary': summary
        }
    }), 200