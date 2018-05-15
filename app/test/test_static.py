from __future__ import absolute_import, unicode_literals

import unittest

from main import app
from os import listdir
from os.path import dirname, isfile, join, normpath, realpath

class StaticFileTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.test_files = self.load_static_files()
    
    def load_static_files(self):
        test_files = {}
        test_dir = dirname(realpath(__file__))

        for file_type in ['js', 'css', 'media']:
            file_path = normpath(test_dir + '/../static/' + file_type) 
            onlyfiles = [f for f in listdir(file_path) if isfile(join(file_path, f))]

            test_files[file_type] = onlyfiles
            
        return test_files
    
    def test_static_html_file(self):
        endpoint = '/'
        response = self.app.get(endpoint)

        self.assertEqual(response.status_code, 200)

    def test_static_js_file(self):
        target_files = self.test_files['js']

        for target_file in target_files:
            endpoint = '/public/js/{0}'.format(target_file)
        
            response = self.app.get(endpoint)

            self.assertEqual(response.status_code, 200)
    
    def test_static_css_file(self):
        target_files = self.test_files['css']

        for target_file in target_files:
            endpoint = '/public/css/{0}'.format(target_file)
        
            response = self.app.get(endpoint)

            self.assertEqual(response.status_code, 200)

    def test_static_media_file(self):
        target_files = self.test_files['media']

        for target_file in target_files:
            endpoint = '/public/media/{0}'.format(target_file)
        
            response = self.app.get(endpoint)

            self.assertEqual(response.status_code, 200)
    
    