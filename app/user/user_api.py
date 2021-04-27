from flask import Blueprint, request, jsonify
# 创建一个蓝图对象（蓝图使用第1步）
userApi = Blueprint('userApi', __name__)


# 获取用户列表
@userApi.route('/getUserList', methods=['GET', 'POST'])
def getUserList():
    arr = []
    with open(r"D:\python\myproject\file\user.txt", "r", encoding='UTF-8') as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            arr.append(line)
    msg = {
        "data": arr
    }
    return jsonify(msg)


# 增加用户
@userApi.route('/addUser', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        print(data)
        print(username)
        with open(r"D:\python\myproject\file\user.txt", "a", encoding='UTF-8') as f:
            f.write("\n"+username)
    msg = {
        "msg": '用戶{}添加成功!'.format(username)
    }
    return jsonify(msg)
