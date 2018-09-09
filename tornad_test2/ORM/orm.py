from tornado.web import RequestHandler


class ORM(RequestHandler):
    def save(self):
        sql = ""
        self.application.db.insert(sql)

    def delete(self):
        pass

    def update(self):
        pass

    def all(self):
        pass

    def filter(self):
        pass
