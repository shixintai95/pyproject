from tornado.web import RequestHandler, authenticated


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.write("index")


class CookieHandler(RequestHandler):
    # 设置cookie
    def get(self, *args, **kwargs):
        self.set_cookie("sunck","good")
        self.write("OK")


class GetCookieHandler(RequestHandler):
    # 获取cookie
    def get(self, *args, **kwargs):
        cookie = self.get_cookie("sunck",default="未登录")
        print("cookie:%s" % cookie)
        self.write("get cookie")


class ClearCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 清除一个cookie
        self.clear_cookie("sunck")
        # 清除所有cookie
        # self.clear_all_cookies()
        self.write("clear OK")


class SCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 设置安全cookie
        self.set_secure_cookie("atai", "cool")
        self.write("OK")


class GSCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 获取设置的安全cookie
        g = self.get_secure_cookie("atai")
        print(g)

        self.write("OKK")


class CookieNumHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # cookie计数
        count = self.get_cookie("count", "未登录")
        if not count:
            count = 1
        # else:
        #     count = int(count)
        #     count += 1
        self.set_cookie("count", str(count))
        self.render("cookienum.html", count=count)


class PostFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("postfile.html")

    def post(self, *args, **kwargs):
        # cookie计数
        count = self.get_cookie("count", None)
        if not count:
            count = 1
        else:
            count = int(count)
            count += 1
        self.set_cookie("count", str(count))
        self.render("cookienum.html", count=count)


# 用户验证
class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        next = self.get_argument("next", "/")
        url = "login?next=" + next
        self.render('login.html', url=url)

    def post(self, *args, **kwargs):
        name = self.get_argument("username")
        password = self.get_argument("password")
        if name == '1' and password == '1':
            next = self.get_argument("next", "/")
            self.redirect(next + "?flag=logined")
        else:
            next = self.get_argument("next", "/")
            self.redirect("/login?next=" + next)


class HomeHandler(RequestHandler):

    @authenticated
    def get(self, *args, **kwargs):
        self.render("home.html")

    def get_current_user(self):
        # /home
        next = self.get_argument("flag", None)
        return next


class CartHandler(RequestHandler):

    @authenticated
    def get(self, *args, **kwargs):
        self.render("cart.html", title="cart")

    def get_current_user(self):
        # /home
        next = self.get_argument("flag", None)
        return next







