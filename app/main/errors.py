#coding:utf8
from flask import render_template
from . import main
u'''
专门用以处理error

'''
@main.app_errorhandler(404)
def h404(e):
    return  'error 404'

