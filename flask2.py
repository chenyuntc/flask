import json

from flask import Flask, redirect, url_for, request, jsonify, make_response
from flask.ext.mysqldb import MySQL
from flask.ext.httpauth import HTTPBasicAuth


import default_config

auth=HTTPBasicAuth()



app = Flask(__name__)
app.config.from_object(default_config)

mysql = MySQL(app)

@auth.get_password
def get_passwd(username):
    if username=='ok':
        return 'python'
    return None

@auth.error_handler
def unauthorize():
    return make_response(jsonify({'error':'unauthorize'}),403)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/todo/api/v1.0/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    cur = mysql.connection.cursor()
    sql = 'select * from task where id=%s' % task_id
    if task_id:
        cur.execute(sql)
    else:
        cur.execute('select * from task ')
    res = cur.fetchall()
    ret = {}
    cur.close()
    if len(res) == 0:
        u = url_for('error404', error='id not fount')
        return redirect(u)

    i = 0
    real_ret = {}
    for task in res:
        i += 1
        ret['id'] = task[0]
        ret['detail'] = task[1]
        ret['done'] = (task[2] == True)
        ret['title'] = task[3]
        real_ret[i] = ret
    return json.dumps(real_ret)


@app.route('/tood/v1.0/<error>')
@app.errorhandler(404)
def error404(error):
    e = {'id': 'error', 'detail': str(error)}
    return json.dumps(e), 404


@app.route('/todo/api/v1.0/task', methods=['POST'])
def add_task():
    c = mysql.connect
    cur = c.cursor();
    try:
        detail = request.json.get('detail', None)
        title = request.json.get('title')
        id = request.json.get('id', None)
        sql = 'insert into task(description,title,done) value("%s", "%s",0)' % (detail, title)
        cur.execute(sql)
        c.commit()
    except Exception as e:
        return jsonify({'result':'fail','error':str(e)})

    return jsonify({'result':'success'})


@app.route('/todo/api/v1.0/task')
@auth.login_required
def get_all_task():
    conn = mysql.connect
    cur = conn.cursor()
    sql = 'select * from task'
    cur.execute(sql)
    ret = {};
    i = 0
    for ii in cur:
        tmp = {}
        i += 1
        tmp['id'] = ii[0]
        tmp['detail'] = ii[1]
        tmp['done'] = (ii[2] == 1)
        tmp['title'] = ii[3]
        ret[i] = tmp
    return json.dumps(ret)


if __name__ == '__main__':
    app.run()
