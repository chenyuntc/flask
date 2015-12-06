#coding:utf8
from flask import  Flask
from flask.ext.mysqldb import MySQL
from flask.ext.httpauth import HTTPBasicAuth
from config import config
import time
m=MySQL()
## 在m不指定app时, 在创建connect时,会自动从current_app获取config

'''markdown
大部分的flask扩展都支持
m=Extention()
m.init_app(app)
的操作
之所以先创建再初始化, 是为了避免重复绑定
1 每次import 的时候都会执行m=Mysql() 乳沟直接制定app的话很麻烦
2 如果m卸载代码块里面, 其他文件中就无法import m了

'''
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from main import main_blue as main_blueprint
    app.register_blueprint(main_blueprint)
    from blue2 import blue2s as b

    app.register_blueprint(b)
    print "-----------first------------------------------%s" %str(time.time())
    #m.init_app(app)
    return app

