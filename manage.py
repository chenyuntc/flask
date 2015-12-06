#coding:utf8

'''
manager 主程序, 用以引导app
可以修改default 来制定运行环境
注意每次引入app 都会创建app 执行create_app()
'''

# print 'use app'
# print __file__
# print __name__

from app import create_app
app=create_app('default')
if __name__ == '__main__':
    app.run()

