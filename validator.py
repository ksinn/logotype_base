#!/usr/local/bin/python
#coding: utf-8
from param import titles
from brend import (required_field_list as brend_required_field_list,
int_field_list as brend_int_field_list,
string_field_list as brend_string_field_list)
from logotypes import (required_field_list as logo_required_field_list,
int_field_list as logo_int_field_list,
string_field_list as logo_string_field_list)

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

