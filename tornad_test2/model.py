from ORM.orm import ORM


class Student(ORM):
    def __init__(self, name, age):
        self.name = name
        self.age = age
