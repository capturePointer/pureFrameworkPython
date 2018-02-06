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

class base:
    def url(self,uri):
        return config.websitePath + "/" + uri

    def assign(self,name,value):
        vars = globalBox.getValue('vars')
        if None == vars:
            vars = {}
        vars[name] = value
        globalBox.setValue('vars',vars)
        return True

    def display(self,tplName):
        start_response = globalBox.getValue('start_response')
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        # 载入模板文件 templates/site.html
        tplNameFull = tplName + ".html"
        templateLoader = FileSystemLoader( searchpath="templates/" )
        templateEnv = Environment( loader=templateLoader )
        template = templateEnv.get_template(tplNameFull)
        # template.render() 返回包含渲染后html的字符串
        vars = globalBox.getValue('vars')
        if vars:
            htmlOutput = template.render(vars).encode( "utf-8" )
        else:
            htmlOutput = template.render().encode( "utf-8" )
        return htmlOutput
