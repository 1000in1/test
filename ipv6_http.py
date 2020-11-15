
import http.server
import socketserver
import socket
class HTTPServerV6(http.server.HTTPServer):
  address_family = socket.AF_INET6

Handler = http.server.SimpleHTTPRequestHandler
server = HTTPServerV6(('::', 8081), Handler)
server.serve_forever()


