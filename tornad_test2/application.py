from tornado import web
import os

from views import index
import config
from ORM.sunckMysql import SunckMySQL


class Application(web.Application):

    def __init__(self):
        handlers = [
            # (r'/', index.IndexHandler),
            (r'/jsontest', index.JsonHandler),
            # 渲染
            (r'/home', index.HomeHandler),
            # 转义
            (r'/trans', index.TransHandler),
            # 继承
            (r'/cart', index.CartHandler),
            # 连接数据库
            (r'/student', index.StudentHandler),
            # StaticFileHandler要放在所有路由的最下面
            (r'/(.*)$', web.StaticFileHandler,
             {"path": os.path.join(config.BASE_PATH, "static/html"),
              "default_filename": "index.html"}),

        ]
        super().__init__(handlers, **config.settings)
        self.db = SunckMySQL(config.mysql["host"], config.mysql["user"],
                             config.mysql["passwd"], config.mysql["dbName"])