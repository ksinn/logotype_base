#!/usr/local/bin/python
#coding: utf-8

from param import database as db_param
import psycopg2

def select(qry_str, param):
    conn = psycopg2.connect(dbname=db_param['db_name'], user=db_param['username'], password=db_param['password'], host=db_param['host'])
    conn.set_client_encoding('UNICODE')
    cursor = conn.cursor()
    cursor.execute(qry_str, param)
    result=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return result

def execute(qry_str, param):
    conn = psycopg2.connect(dbname=db_param['db_name'], user=db_param['username'], password=db_param['password'], host=db_param['host'])
    conn.set_client_encoding('UNICODE')
    cursor = conn.cursor()
    cursor.execute(qry_str, param)
    conn.commit()
    cursor.close()
    conn.close()

