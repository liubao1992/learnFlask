from flask import Blueprint, request, jsonify
import json



# 创建一个蓝图对象（蓝图使用第1步）
loginApi = Blueprint('loginApi', __name__)

#登录
@loginApi.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = json.loads(request.get_data())
        #print(data)
        #print(data['name'])
        return do_the_login(data)
    else:
        print('get login')
        return show_the_login_form()
def do_the_login(data):
    msg = {
        "msg":'post login',
        "data":data
    }
    return jsonify(msg)
def show_the_login_form():
    txt = 'get login'
    return txt