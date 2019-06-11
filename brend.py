#!/usr/local/bin/python
#coding: utf-8

required_field_list = {'id', 'title', 'product', 'industry', 'founded'}
int_field_list = [{'name':'id','min':1,'max':2147483647},
                    {'name':'founded','min':1860,'max':2025}]
string_field_list = [{'name':'title','min':1,'max':100},
                       {'name':'site','min':2,'max':255},
                       {'name':'product','min':1,'max':100},
                       {'name':'industry','min':1,'max':100}]

