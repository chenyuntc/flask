#coding:utf8_
_author__ = 'cy'
from flask import Blueprint
#### 顺序很重要
'''
如果先import view 的话,
import view 的时候又会import blue2s, 然而此时blue2s 不存在 故而出错
'''
blue2s=Blueprint('blue2',__name__);
import view

###