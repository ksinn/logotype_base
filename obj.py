#!/usr/local/bin/python
#coding: utf-8

from psycopg2 import sql
import db

field_list = {'brend':['id','title', 'site', 'product', 'industry', 'founded'],
              'logotype':['id', 'brend_id', 'high', 'width', 'type', 'img']}
operations = {'more':'>', 'less':'<', 'equel':'=', 'between':'between'}


def _to_map(table, rows):
    arr = []
    for row in rows:
        obj={}
        for i in range(len(row)):
            obj[field_list[table][i]] = row[i]
        arr.append(obj)
    return arr
        

def select_all(table):
    qry_str = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table))
    res = db.select(qry_str, [])
    return _to_map(table, res)

def select_one(table, id):
    qry_str = sql.SQL("SELECT * FROM {} WHERE id=%s").format(sql.Identifier(table))
    res = db.select(qry_str, [id])
    arr = _to_map(table, res)
    if len(arr)>0:
        return arr[0]

def delete(table, id):
    qry_str = sql.SQL("DELETE FROM {} WHERE id=%s").format(sql.Identifier(table))
    db.execute(qry_str, [id])

def insert(table, obj):
    obj.pop('id', 0)
    qry_str = sql.SQL("INSERT INTO {} ({}) VALUES ({}) RETURNING id").format(
        sql.Identifier(table),
        sql.SQL(', ').join(map(sql.Identifier, obj.keys())),
        sql.SQL(', ').join(sql.Placeholder() * len(obj))
        )
    res = db.select(qry_str, obj.values())
    obj['id'] = res[0][0]


def update_brend(id, obj):
    qry_str = "UPDATE brend SET ";
    par=[]
    for field in obj.keys():
        qry_str+=" "+field+" = %s,"
        par.append(obj[field])
    qry_str = qry_str[:-1]
    qry_str += " WHERE id = %s"
    par.append(id) 
    db.execute(qry_str, par)

def update_logo(id, obj):
    obj['id'] = id
    qry_str = "UPDATE logotype SET ";
    par=[]
    for field in obj.keys():
        qry_str+=" "+field+" = %s,"
        par.append(obj[field])
    qry_str = qry_str[:-1]
    qry_str += " WHERE id = %s"
    par.append(id) 
    db.execute(qry_str, par)

def search(table, params):
    qry_str = "SELECT * from "+table+" WHERE ";
    if len(params)==0:
        qry_str = qry_str[:-6]    
    for param in params:
        qry_str+=" "+param['field']+" "+operations[param['operator']]+ " "
        if param['operator'] == operations['between']:
            qry_str+=param['value'][0] + " and " + param['value'][1]
        else:
            qry_str+=param['value']
        qry_str+=" and" 
    qry_str = qry_str[:-3]
    res = db.select(qry_str, [])
    return _to_map(table, res)
