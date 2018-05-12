#coding:gbk

import tornado.ioloop
import tornado.web

import subprocess

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        content = subprocess.getoutput('d: & dir')
        html_content = "<html><body>%s<\body><\html>"% content
        self.write(html_content)
#        self.write("Hello, world")

class Test_lijngkuan(tornado.web.RequestHandler):
    def get(self):
        content = subprocess.getoutput('f: & dir')
        html_content = "<html><body>%s<\body><\html>"% content
        self.write(html_content)
#        self.write("Hello, world")

def make_app():       #控制器函数
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/lijingkuan", Test_lijngkuan),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()  #启动服务