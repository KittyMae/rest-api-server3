import os
import io
import pytest
import requests
import json
from urllib.parse import urlencode

@pytest.mark.parametrize("filename,filedata", [("test.txt", "unicorn dragon fairy dragon")])
def test_store_file(app, client, filename, filedata):
    data = {'filename': filename}
    data['file'] = (io.BytesIO(filedata.encode('ascii')), filename)
    response = client.post("/api/v1/store-file", data=data, content_type='multipart/form-data')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'test.txt')
    with open(filepath) as input_file:
        saved_filedata = input_file.read()
    assert response.status_code == 201
    assert os.path.isfile(filepath) == True
    assert saved_filedata == filedata


retrieve_histogram_positive_testdata = [
    ("animals.txt", "dog", 3),
    ("animals.txt", "camel", 2),
    ("animals.txt", "mouse", 1),
    ("animals.txt", "goose", 0),
    ("fruits.txt", "plum", 3),
    ("fruits.txt", "apple", 2),
    ("fruits.txt", "peach", 1),
    ("fruits.txt", "raspberry", 0)
]

@pytest.mark.parametrize("filename,text,expected_occurences", retrieve_histogram_positive_testdata)
def test_retrieve_histogram(client, filename, text, expected_occurences):
    args = urlencode({'filename': filename, 'text': text})
    response = client.get("/api/v1/retrieve-histogram?" + args)
    output = json.loads(response.get_data(as_text=True))
    assert response.status_code == 201
    assert output['occurences'] == expected_occurences

retrieve_histogram_negative_testdata = [
    ("dinosaurs.txt", "T-Rex"),
    ("starwars.txt", "Yoda")
]

@pytest.mark.parametrize("filename,text", retrieve_histogram_negative_testdata)
def test_retrieve_histogram_check_status_code_equals_400(client, filename, text):
    args = urlencode({'filename': filename, 'text': text})
    response = client.get("/api/v1/retrieve-histogram?" + args)
    assert response.status_code == 400

replace_text_positive_testdata = [
    ("animals.txt", "dog", "cat", 3, "mouse cat cat cow cat elephant cat camel cow camel"),
    ("fruits.txt", "peach", "blueberry", 1, "strawberry apple plum apricot plum cherry grapes apple plum blueberry")
]

@pytest.mark.parametrize("filename,text,replacement,expected_replacement_occurences, expected_filedata", replace_text_positive_testdata)
def test_replace_text(app, client, filename, text, replacement, expected_replacement_occurences, expected_filedata):
    data = {'filename': filename, 'text': text, 'replacement': replacement}
    response = client.post("/api/v1/replace-text", data=data, content_type='multipart/form-data')
    output = json.loads(response.get_data(as_text=True))
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(filepath) as input_file:
        filedata = input_file.read()
    assert response.status_code == 201
    assert output['replacedOccurences'] == expected_replacement_occurences
    assert filedata == expected_filedata

replace_text_negative_testdata = [
    ("starwars.txt", "Yoda", "Jar Jar Binks"),
    ("universities.txt", "MU", "VUT")
]

@pytest.mark.parametrize("filename,text,replacement", replace_text_negative_testdata)
def test_replace_text_check_status_code_equals_400(client, filename, text, replacement):
    data = {'filename': filename, 'text': text, 'replacement': replacement}    
    response = client.post("/api/v1/replace-text", data=data, content_type='multipart/form-data')
    output = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400

@pytest.mark.parametrize("filename", ["animals.txt", "fruits.txt"])
def test_delete_file_check_status_code_equals_201(app, client, filename):
    data = {'filename': filename}  
    response = client.post("/api/v1/delete-file", data=data, content_type='multipart/form-data')
    output = json.loads(response.get_data(as_text=True))
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    assert response.status_code == 201
    assert os.path.isfile(filepath) == False

@pytest.mark.parametrize("filename", ["starwars.txt", "universities.txt"])    
def test_delete_file_check_status_code_equals_400(client, filename):
    data = {'filename': filename}  
    response = client.post("/api/v1/delete-file", data=data, content_type='multipart/form-data')
    output = json.loads(response.get_data(as_text=True))    
    assert response.status_code == 400
