__author__ = 'cy'

import os
bashdir=os.path.abspath(os.path.dirname(__file__))

class Config:


    def __init__(self):
        pass


    MYSQL_HOST='127.0.0.1'
    MYSQL_PASSWORD='123456'
    MYSQL_USER='root'
    MYSQL_DB='flask'
    MYSQL_PORT=3306
#MYSQL_CHARSET

    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG=True

class TestConfig(Config):
    DEBUG=True
    MYSQL_DB='test'

config={
    'dev':DevelopmentConfig,
    'test':TestConfig,
    'default':DevelopmentConfig


}