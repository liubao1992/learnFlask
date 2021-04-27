from flask import Blueprint, request, jsonify
import json



# 创建一个蓝图对象（蓝图使用第1步）
registerApi = Blueprint('registerApi', __name__)



### 注册
@registerApi.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #data = json.loads(request.get_data())
        username = request.args.get('username')
        password = request.args.get('password')
        password2 = request.args.get('password2')
        print(username)
        print(password)
        print(password2)
        if not all([username,password,password2]):
            flash ('参数不完整')
        elif password != password2:
            flash ('两次密码不一致，请重新输入')
        else:
            new_user = Users(username=username,password=password,id=None)
            db.session.add(new_user)
            db.session.commit()
            return ''
    return render_template('register.html')
