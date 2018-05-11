from __future__ import absolute_import, unicode_literals

import unittest

from main import app

class StatusTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_status(self):
        endpoint = 'api/status'
        response = self.app.get(endpoint)

        self.assertEqual(response.status_code, 200)