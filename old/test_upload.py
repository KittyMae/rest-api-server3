#!/usr/bin/env python
from flask import Flask, Request, request
from io import BytesIO
import unittest

RESULT = False

class TestFileFail(unittest.TestCase):

    def test_1(self):

        class FileObj(BytesIO):
            
            def close(self):
                print ('in file close')
                global RESULT
                RESULT = True
        
        class MyRequest(Request):
            def _get_file_stream(*args, **kwargs):
                return FileObj()

        app = Flask(__name__)
        app.debug = True
        app.request_class = MyRequest

        @app.route("/count/", methods=['POST'])
        def upload():
            file = request.files['file']
            print ('in upload handler')
            self.assertIsInstance(
                file.stream,
                FileObj,
            )
            # Note I've monkeypatched werkzeug.datastructures.FileStorage 
            # so it wont squash exceptions
            file.close()
            #f.stream.close()
            return 'ok'

        client = app.test_client()
        resp = client.post(
            '/count/',
            data = {
                'file': (BytesIO('my file contents'), 'hello world.txt'),
            }
        )
        self.assertEqual(
            'ok',
            resp.data,
        )
        global RESULT
        self.assertTrue(RESULT)

    def test_2(self):
        pass
        

if __name__ == '__main__':
    unittest.main()