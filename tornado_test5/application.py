from tornado import web
import os

from views import index
import config


class Application(web.Application):

    def __init__(self):
        handlers = [
            (r'/students', index.StudentsHandler),
            (r'/students2', index.Students2Handler),
            (r'/home', index.HomeHandler),
            # websocket 连接
            (r'/chat', index.ChatHandler),


        ]
        super().__init__(handlers, **config.settings)