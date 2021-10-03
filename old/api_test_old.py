import unittest
import requests
from myapp import app 
import io
import werkzeug
import os


class FlaskTestCase(unittest.TestCase):
    #Flask was setup correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #Count page was setup correctly
    def test_count(self):
        tester = app.test_client(self)
        response = tester.get('/count/', content_type='html/text')
        self.assertTrue(b'WORDCOUNT' in response.data, 200)

    #Replace page was setup correctly
    def test_replace(self):
        tester = app.test_client(self)
        response = tester.get('/replace/', content_type='html/text')
        self.assertTrue(b'WORDREPLACE' in response.data, 200)

    #Delete page was setup correctly
    def test_delete(self):
        tester = app.test_client(self)
        response = tester.get('/delete/', content_type='html/text')
        self.assertTrue(b'Delete' in response.data, 200)




if __name__ == "__main__":
    unittest.main()