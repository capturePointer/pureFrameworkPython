#-*-coding:utf-8 -*-
import sqlite3
import time
from core import globalBox
def __dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getCursor():
    cursor = globalBox.getValue("sqlite3_cursor")
    if cursor is None:
        conn = sqlite3.connect('test.db', isolation_level=None)
        conn.row_factory = __dict_factory
        cursor = conn.cursor()
        #当表不存在时，创建表
        cursor.execute('''CREATE TABLE if not exists node
           (id INTEGER PRIMARY KEY     NOT NULL,
           title           CHAR(1024)    NOT NULL,
           link            CHAR(255)     NOT NULL,
           content      CHAR(255)     NOT NULL,
           create_time     int(10));''')
        globalBox.setValue("sqlite3_conn",conn)
        globalBox.setValue("sqlite3_cursor",cursor)
    return cursor

def close():
    conn = globalBox.getValue("sqlite3_conn")
    conn.close()
    return True

