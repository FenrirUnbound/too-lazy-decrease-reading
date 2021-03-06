from __future__ import absolute_import, unicode_literals

import json
import os
import unittest

from main import app

class SummarizeTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def load_data(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_data = []
        with open('{}/data/test_article'.format(dir_path)) as f:
            content = f.readlines()
            content = [l.strip() for l in content]
            file_data = [l for l in content if len(l) > 0]

        return '\n'.join(file_data)
    
    def test_summarize(self):
        endpoint = 'api/summarize'
        test_data = self.load_data()
        test_payload = {
            'data': test_data
        }
        response = self.app.post(endpoint, data=json.dumps(test_payload))

        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.data)
        self.assertDictContainsSubset({
            'lines': 8
        }, payload['data'])
        self.assertEqual(8, len(payload['data']['summary']))
    
    def test_summarize_specific_algorithm(self):
        endpoint = 'api/summarize?alg=lex_rank'
        test_data = self.load_data()
        test_payload = {
            'data': test_data
        }
        response = self.app.post(endpoint, data=json.dumps(test_payload))

        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.data)
        self.assertDictContainsSubset({
            'lines': 8
        }, payload['data'])
        self.assertEqual(8, len(payload['data']['summary']))
    
    def test_summarize_algorithms_exist(self):
        algorithms = [
            'kl',
            'lex_rank',
            'lsa',
            'text_rank'
        ]

        for alg in algorithms:
            endpoint = 'api/summarize?alg={0}'.format(alg)
            test_data = self.load_data()
            test_payload = {
                'data': test_data
            }
            response = self.app.post(endpoint, data=json.dumps(test_payload))

            self.assertEqual(response.status_code, 200)

    def test_failure_unsupported_algorithm(self):
        endpoint = 'api/summarize?alg=unknown'
        test_data = self.load_data()
        test_payload = {
            'data': test_data
        }
        response = self.app.post(endpoint, data=json.dumps(test_payload))

        self.assertEqual(response.status_code, 400)
        payload = json.loads(response.data)
        self.assertEqual('Unknown summary algorithm: unknown', payload['error'])
        
        