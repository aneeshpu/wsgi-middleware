from wsgiref.simple_server import make_server

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

all_caps_middleware = AllCaps(app)
httpd = make_server("localhost", 8000, all_caps_middleware)
httpd.serve_forever()
