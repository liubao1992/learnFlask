from flask import Blueprint, request, jsonify
import json,os



# 创建一个蓝图对象（蓝图使用第1步）
uploadFileApi = Blueprint('uploadFileApi', __name__)


### 获取上传文件
@uploadFileApi.route('/uploadFile/', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        #f.save(os.path.join)
    return 'file uploaded successfully'

### 获取指定文件列表
@uploadFileApi.route('/getFiles/', methods=['GET', 'POST'])
def getFiles():
    return 'file uploaded successfully'
