#!/usr/local/bin/python
#coding: utf-8

from flask import Flask, jsonify, send_file, make_response, request, abort
import base64, validator, obj
from param import titles, server as server_param

app = Flask(__name__)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(405)
def not_method_not_allowed(error):
    return make_response(jsonify({'error': 'Method Not Allowed'}), 405)

@app.errorhandler(500)
def not_internal_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

@app.route('/brends', methods=['POST'])
def add_brends():
    validate_result = validator.check_brend(request.json)
    if validate_result['result']!=titles['allow']:
        request.json['error'] = validate_result
        return jsonify(request.json), 422
    else:
        obj.insert('brend', request.json)
        return jsonify(request.json), 201
    

@app.route('/brends', methods=['GET'])
def get_brends():
    return jsonify(obj.select_all('brend'))

@app.route('/brends/<int:brend_id>', methods=['GET'])
def get_brend(brend_id):
    brend = obj.select_one('brend', brend_id)
    if not brend:
        abort(404)
    return jsonify(brend)

@app.route('/brends/<int:brend_id>', methods=['PUT'])
def update_brend(brend_id):    
    request.json['id']=brend_id;
    validate_result = validator.check_brend(request.json)
    if validate_result['result']!=titles['allow']:
        request.json['error'] = validate_result
        return jsonify(request.json), 422
    else:
        obj.update_brend(brend_id, request.json)
        return jsonify(request.json)

@app.route('/brends/<int:brend_id>', methods=['DELETE'])
def delete_brend(brend_id):
    obj.delete('brend', brend_id)
    return jsonify({'result': 'True'})

@app.route('/logotypes', methods=['POST'])
def add_logo():
    validate_result = validator.check_logo(request.json)
    if validate_result['result']!=titles['allow']:
        request.json['error'] = validate_result
        return jsonify(request.json), 422
    else:
        obj.insert('logotype', request.json)
        return jsonify(request.json), 201

@app.route('/logotypes', methods=['GET'])
def get_logos():
    return jsonify(obj.select_all('logotype'))

@app.route('/logotypes/<int:logo_id>', methods=['GET'])
def get_logo(logo_id):
    logo = obj.select_one('logotype', logo_id)
    if not logo:
        abort(404)
    return jsonify(logo)

@app.route('/logotypes/<int:logo_id>', methods=['PUT'])
def update_logo(logo_id):
    request.json['id']=logo_id;
    validate_result = validator.check_logo(request.json)
    if validate_result['result']!=titles['allow']:
        request.json['error'] = validate_result
        return jsonify(request.json), 422
    else:
        obj.update_logo(logo_id, request.json)
        return jsonify(request.json)

@app.route('/logotypes/<int:logo_id>', methods=['DELETE'])
def delete_logo(logo_id):
    obj.delete('logotype', logo_id)
    return jsonify({'result': 'True'})

@app.route('/brends/<int:brend_id>/logotypes', methods=['GET'])
def get_logos_by_brend(brend_id):    
        return jsonify(obj.search('logotype', [{'field':'brend_id',
                                'operator':'equel',
                                'value': str(brend_id)}]))
    
@app.route('/brends/search', methods=['post'])
def search_brend():
    validate_result = validator.check_search(request.json)
    for vr in validate_result:
        if vr['result'] !=titles['allow']:
            return jsonify(request.json), 422
    return jsonify(obj.search('brend', request.json))

@app.route('/logotypes/search', methods=['post'])
def search_logo():
    validate_result = validator.check_search(request.json)
    for vr in validate_result:
        if vr['result'] !=titles['allow']:
            return jsonify(request.json), 422
    return jsonify(obj.search('logotype', request.json))
    
if __name__ == '__main__':
    app.run(host = server_param['host'],port=server_param['port'])
