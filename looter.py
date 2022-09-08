from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
    def do_POST(self):
        self.send_response(200)
        print('ok')
        print(self.rfile.read())

    def create_path(self):
        pass

with HTTPServer(('', 443), handler) as server:
    server.socket = ssl.wrap_socket (server.socket, 
        keyfile="code.key", 
        certfile='code.crt', server_side=True)
    print('ok')
    server.serve_forever()