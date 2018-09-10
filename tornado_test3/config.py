import os

BASE_PATH = os.path.dirname(__file__)

options = {
    "port": 8000,
}

mysql = {
    "host": "127.0.0.1",
    "user": "root",
    "passwd": "sxt123123",
    "dbName": "test",
}

settings = {
    "static_path": os.path.join(BASE_PATH, 'static'),
    "template_path": os.path.join(BASE_PATH, "templates"),
    # "autoreload": True,
    "debug": True,
    # 自动转义，设置为None会关闭整个项目的自动转义，一般不会使用
    # "autoescape": None,
}


# CREATE TABLE `students` (
#   `id` int NOT NULL auto_increment,
#   `name` varchar(20) NOT NULL,
#   `age` tinyint NOT NULL,
#   PRIMARY KEY  (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
