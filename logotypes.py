#!/usr/local/bin/python
#coding: utf-8

required_field_list = {'id', 'brend_id', 'img'}

int_field_list = [{'name':'id','min':1,'max':2147483647},
                  {'name':'brend_id','min':1,'max':2147483647},
                  {'name':'high','min':5,'max':1024},
                  {'name':'width','min':5,'max':1024}]

string_field_list = [{'name':'type','min':1,'max':7},
                       {'name':'img','min':1,'max':2147483647255}]
