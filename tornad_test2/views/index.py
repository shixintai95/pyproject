from tornado.web import RequestHandler


class IndexHandler(RequestHandler):

    def initialize(self):
        print("1")

    def prepare(self):
        print("2")

    # def get(self, *args, **kwargs):
    #     print("3")
    #     self.write("服务器内部错误")
    #     self.send_error(404)
    def get(self, *args, **kwargs):
        print("3")
        self.write("get")

    def set_default_headers(self):
        print("4")

    def write_error(self, status_code, **kwargs):
        print("5")

    def on_finish(self):
        print("6")


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        temp = 100

        stus = [
            {
                "name": "zhangsan",
                "age": 22
            },
            {
                "name": "lisi",
                "age": 33
            }
        ]

        # 传递函数
        def ms(n1, n2):
            return n1 + n2

        self.render('home.html', num=temp, flag=1, stus=stus, ms=ms)


# 自动转义，为了防止恶意攻击
class TransHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h1>sunck is a good man</h1>"
        self.render('trans.html', str=str)


class CartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('cart.html', title='给我无耻')


class StudentHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 从数据库中提取数据
        # stus = self.application.db.get_all_obj("select * from students", "students")
        # 查询个别列
        stus = self.application.db.get_all_obj("select name,age from students", "students", "name", "age")
        print(stus)
        # self.application.db.insert("insert into students(name,age) values('uzi','21')")
        # self.write("ok")
        self.render("student.html", stus=stus)