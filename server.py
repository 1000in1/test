
import http.server
import socketserver
import socket
import urllib



class HTTPServerV6(http.server.HTTPServer):
  address_family = socket.AF_INET6



class ServerHTTP(http.server.BaseHTTPRequestHandler):

    getHandler={}
    postHandler={}
    def do_GET(self):
        path = self.path
        #print('path:',path)
        #拆分url(也可根据拆分的url获取Get提交才数据),可以将不同的path和参数加载不同的html页面，或调用不同的方法返回不同的数据，来实现简单的网站或接口
        query = urllib.parse.urlparse(path)
        #query.hostname
        #print('urlparse path',query)
        #print('query',query.path)
  
        if query.path in self.getHandler.keys():
          self.getHandler[query.path](self)
        else:
          self.send_error(404,'not found!') 


        #print(urllib.parse.parse_qs(query.query))
        #print(urllib.parse.parse_qsl(query.query))

        
    def do_POST(self):
        path = self.path
        query = urllib.parse.urlparse(path)
        
        
        if query.path in self.postHandler.keys():
          self.postHandler[query.path](self)
        else:
          self.send_error(404,'not found!') 


    
    
    
    
        

    def init(self,p,m):
      def decorator(fc):
        if 'GET' in m:
          self.getHandler[p]=fc
        if 'POST' in m:
          self.postHandler[p]=fc
        
        #print(self.pathAction)
      return decorator

#Handler = http.server.SimpleHTTPRequestHandler

@ServerHTTP.init(ServerHTTP,"/",['GET'])
def func1(self):
  path = self.path
  #print('path:',path)
  #拆分url(也可根据拆分的url获取Get提交才数据),可以将不同的path和参数加载不同的html页面，或调用不同的方法返回不同的数据，来实现简单的网站或接口
  query = urllib.parse.urlparse(path)
  
  self.send_response(200)
  self.send_header("Content-type","text/html")
  self.send_header("test","This is test!")
  self.end_headers()
  buf = '''<!DOCTYPE HTML>
          <html>
          <head><title>Get page</title></head>
          <body>
          %s
          %s
          </body>
          </html>'''%(self.path,query.hostname)
  self.wfile.write(buf.encode(encoding="utf-8"))


@ServerHTTP.init(ServerHTTP,"/",['POST'])
def func2(self):
    path = self.path
    print(path)
    print(self.headers)
    name = self.headers['n']
    print(name)
    cmd = self.headers['cmd']
    print(cmd)

    query = urllib.parse.urlparse(path)
    print('query',query)
        
    #获取post提交的数据
    fo = open("../share/%s"%name, "wb")
    le = int(self.headers['content-length'])


    self.send_response(200)
    self.send_header("Content-type","text/html")
    self.send_header("test","This is test!")
    self.end_headers()

    buf = '''<!DOCTYPE HTML>
    <html>
        <head><title>Post page</title></head>
        <body>file:%s  <br />size:%d'''%(name,le)
    self.wfile.write(buf.encode(encoding="utf-8"))

    l = 0
    while l<le:
      i=1024
      if l+1024>le:
        i = le-l

      datas = self.rfile.read(i)
      l = l+len(datas)
      line = fo.write( datas )
      buf = '%d/%d<br>'%(l,le)
      print(buf)
      self.wfile.write(buf.encode(encoding="utf-8"))

    fo.close()

    
    buf = '''</body>
    </html>'''
    self.wfile.write(buf.encode(encoding="utf-8"))

    




server = HTTPServerV6(('::', 8081), ServerHTTP)
server.serve_forever()


