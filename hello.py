from wsgiref.simple_server import make_server

def makeapp(f):
    def wrapped_func(env, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain'), ('random-nonsense', 'yeah works')]
        start_response(status, response_headers)

        return f()

    return wrapped_func


@makeapp
def func():
    return ["Hello func"]

def app(env, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]

    start_response(status, response_headers)

    response_body = "Hello World"
    return [response_body]


class AllCaps:
    def __init__(self, app):
        self.app = app

    def __call__(self, env, start_response):
        resp =  self.app(env, start_response)
        resp = [r.upper() for r in resp]
        return resp

httpd = make_server("localhost", 8000, func)
httpd.serve_forever()
