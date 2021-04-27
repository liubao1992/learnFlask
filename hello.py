from app.login import login_api
from app.user import user_api
from app.upload import uploadFile_api
import os
# redirect重定向,request返回请求，jsonify转成json对象
from flask import Flask, json, jsonify, redirect, request, flash
from flask_cors import *
app = Flask(__name__)
# 允许跨域
CORS(app, supports_credentials=True)
app.register_blueprint(user_api.userApi, url_prefix='/user')
app.register_blueprint(login_api.loginApi, url_prefix='/login')
app.register_blueprint(uploadFile_api.uploadFileApi, url_prefix='/upload')

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/redir')
def redir():
    return redirect('https://www.baidu.com')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
