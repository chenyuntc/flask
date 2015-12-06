from . import main
from flask import jsonify
from app import m
from  flask3 import app
@main.route('/')
def hello():

    conn=m.connect
    #conn=app.mysql.connect
    cur=conn.cursor()
    cur.execute('select * from task')
    ret=cur.fetchall()
    return jsonify({'tasks':ret})