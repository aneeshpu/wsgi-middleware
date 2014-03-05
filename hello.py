from wsgiref.simple_server import make_server
from webob.dec import wsgify
import webob

@wsgify.middleware
def my_dec(req, app):
    print "inside my_dec"
    print app
    resp = req.get_response(app)
    resp.body = resp.body.upper()
    return resp

    

@wsgify
def func(req):
    print "inside func"
    return webob.Response('wsgified application')

middleware = my_dec(func)
httpd = make_server("localhost", 8000, middleware)
httpd.serve_forever()
