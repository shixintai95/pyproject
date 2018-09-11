from tornado import web
import os

from views import index
import config


class Application(web.Application):

    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            # 普通cookie
            (r'/pcookie', index.CookieHandler),
            (r'/gcookie', index.GetCookieHandler),
            (r'/ccookie', index.ClearCookieHandler),
            # 安全cookie
            (r'/scookie', index.SCookieHandler),
            (r'/gscookie', index.GSCookieHandler),
            # cookie 计数
            (r'/numcookie', index.CookieNumHandler),
            (r'/postfile', index.PostFileHandler),

            # 用户验证
            (r'/login', index.LoginHandler),
            (r'/home', index.HomeHandler),
            (r'/cart', index.CartHandler),


        ]
        super().__init__(handlers, **config.settings)