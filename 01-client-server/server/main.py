from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from http.cookies import SimpleCookie
import json
from socketserver import TCPServer

# This is a small example of how the http.request library works to receive http requests
# being more specific the http methods (GET AND POST)

# GetHandler implements HTTPRequestHandler, which overloads the do_Get method
class GetHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        cookies = SimpleCookie(self.headers.get('Cookie'))

        print(cookies)

        self.send_response(200)
        self.send_header("Content_Type", 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello world')


# PostHandler implements BaseHTTPRequestHandler, which overloads the do_POST method
class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        content_length = int(self.headers['Content-Length'])

        body = self.rfile.read(content_length)

        print(body.decode())

        json_string = json.dumps({"message":"ok"})

        self.send_response(200)
        self.send_header("Content-type", 'application/json')
        self.end_headers()
        self.wfile.write(json_string.encode())


# this is one way to start a simple server
#def run(server_class=HTTPServer, handler_class=PostHandler):
#    server_address = ('', 8000)
#    httpd = server_class(server_address, handler_class)
#    httpd.serve_forever()

#run()


PORT = 8000

if __name__ == "__main__":
    # Note: to use the GetHandler http handler change it to PostHandler 
    start = TCPServer(('localhost', PORT), PostHandler)

    print("serving at port", PORT)

    try:
        start.serve_forever()
    except KeyboardInterrupt:
        pass

    start.server_close()

    print("Finalized serve")
