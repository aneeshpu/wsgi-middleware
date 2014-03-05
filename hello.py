from wsgiref.simple_server import make_server
from webob.dec import wsgify
import webob

@wsgify
def func(req):
    return webob.Response('wsgified application')

httpd = make_server("localhost", 8000, func)
httpd.serve_forever()
