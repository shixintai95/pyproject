import os

BASE_DIRS = os.path.dirname(__file__)
# 参数
options = {
    "port": 8000
}

# 配置
settings = {
    'static_path': os.path.join(BASE_DIRS, 'static'),
    'template_path': os.path.join(BASE_DIRS, 'templates'),
    # 'debug': True,   # 设置tornado是否工作在调试模式下，默认为false，即工作在生产模式下
    'autoreload': True,
}

