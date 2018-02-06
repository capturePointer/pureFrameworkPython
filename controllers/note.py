# -*- coding: utf-8 -*-Python
import sys
import sqlite3
import time
from core import globalBox
from core import db
import os
import cgi
from urllib.parse import urlparse
from html import escape
from jinja2 import Environment, FileSystemLoader
import sys
from config import config
from controllers.base import base

class note(base):
    def clear(self,env, start_response):
        cursor = db.getCursor()
        cursor.execute("DELETE FROM node")
        cursor.execute("DROP TABLE node")
        start_response('302 Found', [('Location','index')])
        return ["clear success"]

    def index(self,env, start_response):
        lists = []
        cursor = db.getCursor()
        if cursor is not None:
            #查询所有记录
            for row in cursor.execute("SELECT * FROM node ORDER BY id DESC"):
                lists.append(row)
        self.assign("lists",lists)
        self.assign("time",time)
        self.assign("url",self.url)
        htmlOutput = self.display("index")
        return [htmlOutput]

    def add(self,env, start_response):
        htmlOutput = self.display("add")
        return [htmlOutput]

    def doAdd(self,env, start_response):
        def md5(str):
            import hashlib
            m = hashlib.md5()
            m.update(str.encode("utf-8"))
            return m.hexdigest()
        if env['REQUEST_METHOD'] == 'POST':
            post_env = env.copy()
            post_env['QUERY_STRING'] = ''
            post = cgi.FieldStorage(
                fp=env['wsgi.input'],
                environ=post_env,
                keep_blank_values=True
            )
            title = post['title'].value
            link = post['link'].value
            content = post['content'].value
            create_time = str(int(time.time()))
            cursor = db.getCursor()
            if cursor is not None:
                cursor.execute("INSERT INTO node (title,link,content,create_time) \
                    VALUES ('" + title + "', '" + link + "', '" + content +  "', '" + create_time + "')");
        start_response('302 Found', [('Location','index')])
        return ["success"]

    def edit(self,env, start_response):
        d = cgi.parse_qs(env['QUERY_STRING'])
        id = d.get('id', [''])[0]
        cursor = db.getCursor()
        if cursor is not None:
            cursor = cursor.execute("SELECT * FROM node WHERE `id` = " + id)
            data = cursor.fetchone()
        self.assign('data',data)
        htmlOutput = self.display("edit")
        return [htmlOutput]

    def doEdit(self,env, start_response):
        def md5(str):
            import hashlib
            m = hashlib.md5()
            m.update(str.encode("utf-8"))
            return m.hexdigest()
        if env['REQUEST_METHOD'] == 'POST':
            post_env = env.copy()
            post_env['QUERY_STRING'] = ''
            post = cgi.FieldStorage(
                fp=env['wsgi.input'],
                environ=post_env,
                keep_blank_values=True
            )
            id = post['id'].value
            title = post['title'].value
            link = post['link'].value
            content = post['content'].value
            create_time = str(int(time.time()))
            cursor = db.getCursor()
            if cursor is not None:
                cursor.execute("UPDATE node SET `title`='"+ title +"',`link`='"+ link +"'" + ",`content`='"+ content +"'" + ",`create_time`='"+ create_time +"' WHERE `id` = " + id)
        start_response('302 Found', [('Location','index')])
        return ["success"]
