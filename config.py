#coding:utf8

__author__ = 'cy'

import os
bashdir=os.path.abspath(os.path.dirname(__file__))
from flask.ext.mysqldb import MySQL
class Config:


    def __init__(self):
        pass
    MYSQL_HOST='127.0.0.1'
    MYSQL_PASSWORD='123456'
    MYSQL_USER='root'
    MYSQL_DB='flask'
    MYSQL_PORT=3306


    @staticmethod
    def init_app(app):
        print '------------------smg------------------'
        app.mysql = MySQL(app)
        print app.mysql
        #print app.mysql.connect
'''
init_app 是很多flask扩展都支持的一项操作, 可以先创建, 然后调用init_app, 修改app的属性
在此, 不同的环境, 需要对app进行不同的配置(config),config 无法配置的属性, 可以在init_app中写

'''
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