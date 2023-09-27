from flask import Flask,request,render_template,jsonify
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    _db = pymysql.connect(        
        host = 'localhost',
        user ='root',
        password = 'user',
        db = 'os',
        port = 3306    
    )
    cursor = _db.cursor(pymysql.cursors.DictCursor)