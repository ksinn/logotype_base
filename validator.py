#!/usr/local/bin/python
#coding: utf-8
from param import titles

brend_required_field_list = {'title', 'product', 'industry', 'founded'}

brend_int_field_list = [{'name':'id','min':1,'max':2147483647},
                    {'name':'founded','min':1860,'max':2025}]

brend_string_field_list = [{'name':'title','min':1,'max':100},
                       {'name':'site','min':2,'max':255},
                       {'name':'product','min':1,'max':100},
                       {'name':'industry','min':1,'max':100}]

logo_required_field_list = {'brend_id', 'img'}

logo_int_field_list = [{'name':'id','min':1,'max':2147483647},
                  {'name':'brend_id','min':1,'max':2147483647},
                  {'name':'high','min':5,'max':2048},
                  {'name':'width','min':5,'max':2048}]

logo_string_field_list = [{'name':'type','min':1,'max':7},
                       {'name':'img','min':1,'max':2147483647255}]

def _set_invalid(res, field, error):
    res['result'] = titles['failed']
    res[field] = titles[error]

def _validate(obj, required_field_list, int_field_list, string_field_list):
    res = dict()
    res['result'] = titles['allow']

    has_field = set(obj.keys())
    missed_fields = required_field_list - has_field
    for field in missed_fields:
        _set_invalid(res, field, 'no_field')
    
    for field in int_field_list:
        if not field['name'] in obj:
            continue
        if not type(obj[field['name']]) is int:
            _set_invalid(res, field['name'], 'incorrect_type')
        else:
            if obj[field['name']] < field['min'] or obj[field['name']] > field['max']:
                _set_invalid(res, field['name'], 'out_of_range')
    
    for field in string_field_list:
        if not field['name'] in obj:
            continue
        if isinstance(obj[field['name']], str):
            _set_invalid(res, field['name'], 'incorrect_type')
        else:
            if len(obj[field['name']]) < field['min'] or len(obj[field['name']]) > field['max']:
                _set_invalid(res, field['name'], 'out_of_range')
    
    return res

def check_brend(brend):
    return _validate(brend, brend_required_field_list, brend_int_field_list, brend_string_field_list)
    
def check_logo(logo):
    return _validate(logo, logo_required_field_list, logo_int_field_list, logo_string_field_list)

