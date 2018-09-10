from tornado import ioloop, httpserver

from application import Application
import config

if __name__ == "__main__":

    app = Application()
    httpServer = httpserver.HTTPServer(app)
    httpServer.bind(config.options["port"])
    httpServer.start(1)
    ioloop.IOLoop.current().start()