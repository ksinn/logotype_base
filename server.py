#!/usr/local/bin/python
#coding: utf-8

from flask import Flask, jsonify, send_file, make_response, request
import base64

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'Method Not Allowed'}), 405)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

@app.route('/brends', methods=['POST'])
def add_brends():
    return jsonify(request.json), 201

@app.route('/brends', methods=['GET'])
def get_brends():
    return jsonify([{
        'id': 1,
        'title': 'Nescafé',
	'site': 'nescafe.com',
	'product': 'Растворимый кофе',	
        'industry': 'Напитки', 
        'founded': 1938
	}, {
        'id': 2,
        'title': 'Nescafé',
	'site': 'nescafe.com',
	'product': 'Растворимый кофе',	
        'industry': 'Напитки', 
        'founded': 1938
	}])

@app.route('/brends/<int:brend_id>', methods=['GET'])
def get_brend(brend_id):
    return jsonify({
        'id': brend_id,
        'title': 'Nescafé',
	'site': 'nescafe.com',
	'product': 'Растворимый кофе',	
        'industry': 'Напитки', 
        'founded': 1938
	})

@app.route('/brends/<int:brend_id>', methods=['PUT'])
def update_brend(brend_id):    
    request.json['id']=brend_id;
    return jsonify(request.json)

@app.route('/brends/<int:brend_id>', methods=['DELETE'])
def delete_brend(brend_id):
    return jsonify({'result': 'True'})

@app.route('/logotypes', methods=['POST'])
def add_logo():
    return jsonify(request.json), 201

@app.route('/logotypes', methods=['GET'])
def get_logos():
    with open('test_logo.png', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return jsonify([{
        'id': 1,
        'brend_id': 1,
	'high': '128',
	'width': '128',	
        'type': 'png',
        'img': encoded_string
	}, {
        'id': 2,
        'brend_id': 1,
	'high': '128',
	'width': '128',	
        'type': 'png',
        'img': encoded_string
	}])

@app.route('/logotypes/<int:logo_id>', methods=['GET'])
def get_logo(logo_id):
    with open('test_logo.png', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return jsonify({
        'id': logo_id,
        'brend_id': 1,
	'high': '128',
	'width': '128',	
        'type': 'png',
	'img': encoded_string
	})

@app.route('/logotypes/<int:logo_id>', methods=['PUT'])
def update_logo(logo_id):
    request.json['id']=logo_id;
    return jsonify(request.json)

@app.route('/logotypes/<int:logo_id>', methods=['DELETE'])
def delete_logo(logo_id):
    return jsonify({'result': 'True'})

@app.route('/brends/<int:brend_id>/logotypes', methods=['GET'])
def get_logos_by_brend(brend_id):    
        with open('test_logo.png', 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return jsonify([{
        'id': 1,
        'brend_id': brend_id,
	'high': '128',
	'width': '128',	
        'type': 'png',        
	'img': encoded_string
	}, {
        'id': 2,
        'brend_id': brend_id,
	'high': '128',
	'width': '128',	
        'type': 'png',
	'img': encoded_string
	}])


if __name__ == '__main__':
    app.run()
