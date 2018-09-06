from tornado import web
from views import index
import config


class Application(web.Application):

    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/sunck', index.SunckHandler, {"work1": "lala", "work2": "haha"}),
            web.url(r'/avm', index.KaigeHandler, {"word3": "handsom", "age": 12}, name="kaige"),
            (r'/lisi/(\w+)/(\w+)/(\w+)', index.LisiHandler),
            (r'/zhangmanyu', index.ZhangmanyuHandler),
            (r'/json1', index.Json1Handler),
            (r'/json2', index.Json2Handler),
            (r'/index', index.RedirectHandler),
            (r'/error', index.ErrorHandler),
        ]
        super(Application, self).__init__(handlers, **config.settings)