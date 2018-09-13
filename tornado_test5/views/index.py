import tornado
from tornado.web import RequestHandler
from tornado.web import asynchronous
from tornado.websocket import WebSocketHandler
from tornado.httpclient import AsyncHTTPClient
import json


class StudentsHandler(RequestHandler):
    def on_response(self, response):
        if response.error:
            self.send_error(500)
        else:
            data = json.loads(response.body)
            self.write(data)
        self.finish()

    @asynchronous # 不关闭通信通道
    def get(self, *args, **kwargs):
        url = "http://127.0.0.1:8888/jsontest"
        # 创建客户端
        client = AsyncHTTPClient()
        client.fetch(url, self.on_response)


# 协程异步
class Students2Handler(RequestHandler):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = "http://127.0.0.1:8888/jsontest"
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            data = json.loads(res.body)
            self.write(data)


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("home.html")


class ChatHandler(WebSocketHandler):
    users = []

    def open(self, *args, **kwargs):
        self.users.append(self)
        for user in self.users:
            print(user)
            user.write_message(u"[%s]登陆了" % self.request.remote_ip)

    def on_message(self, message):
        for user in self.users:
            user.write_message(u"[%s]说：%s" % (self.request.remote_ip, message))

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            print(user)
            user.write_message(u"[%s]退出了" % self.request.remote_ip)

    def check_origin(self, origin):
        return True


