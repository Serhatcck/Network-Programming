# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:45:43 2020

@author: fikirsanat
"""

from pprint import pformat
from wsgiref.simple_server import make_server

def app(environ,start_response):
    headers = {'Content-Type':'text/plain;charset=utf-8'}
    start_response('200 Ok',list(headers.items()))
    yield 'Here is the WSGI environment:\r\n\r\n'.encode('utf-8')
    yield pformat(environ).encode('utf-8')
    
if __name__ == '__main__':
    httpd = make_server('localhost',8000,app)
    host,port=httpd.socket.getsockname()
    print('Serving on',host,'port',port)
    httpd.serve_forever()
    