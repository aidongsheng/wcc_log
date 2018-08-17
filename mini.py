from flask import Flask,Request,make_response,Response,jsonify,request,logging,app
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)

#配置flask配置对象中键：SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ads---@localhost/database"

#配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#获取SQLAlchemy实例对象，接下来就可以使用对象调用数据
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/getlog',methods=['POST','GET'])
def getlog():
    return jsonify({"name":"dongsheng"})

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=8800)