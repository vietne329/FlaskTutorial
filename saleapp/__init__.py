from flask import Flask

#import flaskSqlAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'SECRETKEY_APP'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mysqllocal:123456@localhost/mysaleapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# tạo biến db
db = SQLAlchemy(app=app)

