"""This is a simple example of running a wsgi application with eventlet.
For a more fully-featured server which supports multiple processes,
multiple threads, and graceful code reloading, see:

http://pypi.python.org/pypi/Spawning/
"""
import re

import eventlet
from eventlet import wsgi

from core import globalBox
from route import route


def app(env, start_response):
    globalBox._init()
    globalBox.setValue('start_response',start_response)
    globalBox.setValue('env',env)
    path = env.get('PATH_INFO', '').lstrip('/')
    for regex, callback in route.routes:
        match = re.search(regex, path)
        if match is not None:
            return callback(env, start_response)
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return ['Not Found\r\n']


if __name__ == '__main__':
    try:
        wsgi.server(eventlet.listen(('0.0.0.0', 8090)), app)
    except KeyboardInterrupt:
        print('see you.')
