from tornado.web import RequestHandler
import config
import os


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url("kaige")
        # self.write("<a href='/sunck'>去另一个界面</a>")
        self.write("<a href='%s'>去另一个界面</a>" % url)


class SunckHandler(RequestHandler):

    def initialize(self, work1, work2):
        self.work1 = work1
        self.work2 = work2

    def get(self, *args, **kwargs):
        print(self.work1, self.work2)
        self.write("nice boy " + self.work1 + self.work2)


class KaigeHandler(RequestHandler):
    def initialize(self, word3, age):
        self.word3 = word3
        self.age = age
        print(self.word3, self.age)

    def get(self, *args, **kwargs):
        self.write("this kaige")


class LisiHandler(RequestHandler):
    def get(self, h1, h2, h3, *args, **kwargs):
        print(h1 + "-" + h2 + "-" + h3)
        self.write("lisi")


class ZhangmanyuHandler(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument("a")
        b = self.get_query_argument("b")
        c = self.get_query_argument("c")
        print(a, b, c)
        self.write("zhangmanyu")


class PostFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postfile.html')

    def post(self, *args, **kwargs):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        hobby = self.get_body_arguments("hobby")
        print(username, password, hobby)
        self.write("post")


class ZhuyinHandler(RequestHandler):

    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)
        self.write("获取请求参数")


class UpfileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('upfile.html')

    def post(self, *args, **kwargs):
        filesDict = self.request.files
        for inputname in filesDict:
            fileArr = filesDict[inputname]
            for fileObj in fileArr:
                filePath = os.path.join(config.BASE_DIRS, 'upfile/', fileObj.filename)
                with open(filePath, 'wb') as f:
                    f.write(fileObj.body)
        self.write("ok")


import json
class Json1Handler(RequestHandler):

    def get(self, *args, **kwargs):
        per = {
            "name": "zhangsan",
            "age": "lisi",
            "sex": 13,
            "num": "112"
        }

        jsonStr = json.dumps(per)
        self.set_header("shixnn","good")
        self.write(jsonStr)


class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "zhangsan",
            "age": "lisi",
            "sex": 33,
            "num": "110"
        }
        self.write(per)


class RedirectHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.redirect("/")

# send_error 和 write_error 合起来使用
class ErrorHandler(RequestHandler):
    def get(self, *args, **kwargs):
        flag = self.get_query_argument('flag')
        if flag == '0':
            self.send_error(404)
        self.write("you are right")

    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            self.write("内部错误")
        elif status_code == 404:
            self.write("不存在")
        self.set_status(status_code)