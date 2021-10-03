import os
from app import app
from flask import Flask, request, jsonify

@app.route('/store-file', methods=['POST'])
def upload_file():
    if 'filename' not in request.form:
        resp = jsonify({'message' : "Missing 'filename' parameter"})
        resp.status_code = 400
        return resp
    if 'file' not in request.files:
        resp = jsonify({'message' : "No file part in the request"})
        resp.status_code = 400
        return resp
    filename = request.form.get('filename')
    file = request.files['file']
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({'message' : "File successfully stored"})
        resp.status_code = 201
        return resp

@app.route('/retrieve-histogram', methods=['GET'])
def retrieve_histogram():
    print(request.args)
    if 'filename' not in request.args:
        resp = jsonify({'message' : "Missing 'filename' parameter"})
        resp.status_code = 400
        return resp    
    if 'text' not in request.args:
        resp = jsonify({'message' : "Missing 'text' parameter"})
        resp.status_code = 400
        return resp
    filename = request.args.get('filename')
    text = request.args.get('text')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.isfile(filepath):
        resp = jsonify({'filename' : filename, 'text' : text, 'message' : "File not found"})
        resp.status_code = 400
        return resp    
    with open(filepath, 'r') as input_file:
        filedata = input_file.read()    
    occurences = filedata.count(text)
    resp = jsonify({'text' : text, 'occurences' : occurences, 'message' : "Histogram successfully retrieved"})
    resp.status_code = 201
    return resp

@app.route('/replace-text', methods=['POST'])
def replace_text():
    if 'filename' not in request.form:
        resp = jsonify({'message' : "Missing 'filename' parameter"})
        resp.status_code = 400
        return resp    
    if 'text' not in request.form:
        resp = jsonify({'message' : "Missing 'text' parameter"})
        resp.status_code = 400
        return resp
    if 'replacement' not in request.form:
        resp = jsonify({'message' : "Missing 'text' parameter"})
        resp.status_code = 400
        return resp
    filename = request.form.get('filename')
    text = request.form.get('text')
    replacement = request.form.get('replacement')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.isfile(filepath):
        resp = jsonify({'filename' : filename, 'text' : text, 'replacement' : replacement, 'message' : "File not found"})
        resp.status_code = 400
        return resp    
    with open(filepath, 'r') as input_file:
        filedata = input_file.read()
    occurences = filedata.count(text)
    filedata = filedata.replace(text, replacement)
    print(filedata)
    with open(filepath, 'w') as output_file:
        output_file.write(filedata)
    resp = jsonify({'filename' : filename, 'text' : text, 'replacement' : replacement, 'replacedOccurences' : occurences, 'message' : "Text successfully replaced"})
    resp.status_code = 201
    return resp

@app.route('/delete-file', methods=['POST'])
def replace():
    print(request.form)
    if 'filename' not in request.form:
        resp = jsonify({'message' : "Missing 'filename' parameter"})
        resp.status_code = 400
        return resp    
    filename = request.form.get('filename')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.isfile(filepath):
        resp = jsonify({'filename' : filename, 'message' : "File not found"})
        resp.status_code = 400
        return resp
    os.remove(filepath)
    resp = jsonify({'filename' : filename, 'message' : "File successfully deleted"})
    resp.status_code = 201
    return resp
