from http.server import BaseHTTPRequestHandler
class Server(BaseHTTPRequestHandler):
  def do_HEAD(self):
    return
  def do_POST(self):
    return
  def do_GET(self):
    self.send_response(200,"MESSEGE TEST")
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(self.path)
    return 
  def handle_http(self):
    return
  def respond(self):
    return
