from http.server import BaseHTTPRequestHandler
import os 
class Server(BaseHTTPRequestHandler):
  def do_HEAD(self):
    return
  def do_POST(self):
    return
  def do_GET(self):
    try:
      if(self.path.endswith(".html")):
        self.send_response(200,"MESSEGE TEST")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        pth=os.path.abspath(os.getcwd())
        pth=pth+self.path
        f=open(pth,"r+")
        self.wfile.write(bytes(f.read(),"UTF-8"))
        f.close()
      elif (self.path.endswith(".css")):
        self.send_response(200,"MESSEGE TEST")
        self.send_header("Content-type", "text/css")
        self.end_headers()
        pth=os.path.abspath(os.getcwd())
        pth=pth+self.path
        f=open(pth,"r+")
        self.wfile.write(bytes(f.read(),"UTF-8"))
        f.close()
    except IOError:
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(bytes("404 not found","UTF-8"))
      self.send_error(404,"NOT FOUND")
    return 
  def handle_http(self):
    return
  def respond(self):
    return
