# 라이브러리 로드
from flask import Flask, render_template, request, jsonify
import pymysql

_db = pymysql.connect(        
        host = 'localhost',
        user ='root',
        password = 'user',
        db = 'os',
        port = 3306    
)

cursor = _db.cursor(pymysql.cursors.DictCursor)

# Flask class 생성
# 생성자함수 인자값 : __name__ 
app = Flask(__name__)

# api 생성
# 네비게이터 : 지정한 주소값으로 요청이 들어왔을 때 아래의 함수를 호출
@app.route('/')
def index():
    return render_template('signup.html')

# 비동기 통신으로 데이터를 받고 보내줄 주소 생성
@app.route('/base_ajax')
def base_ajax():
    # 서버가 db저에게 보내는 데이터를 변수에 대입
    input1 = request.args['_id']
    print(input1)
    data = {
        'name' : 'text',
        'loc' : 'Nowon'
    }
    return jsonify(data)

@app.route('/check_id')
def check_id():
    _id = request.args['input_id']
    sql = """
        SELECT
        *
        FROM
        user_list
        WHERE
        id = %s
        """
        
    cursor.execute(sql,[_id])
    result = cursor.fetchall()
    
    # 아이디가 존재한다면 result 길이가 1
    if (len(result) == 1):
        data = {
            'able' : False
        }
    else :
        data = {
            'able' : True
        }
    return jsonify(data)




# debug 모드(개발자모드)는 개발중에는 서버재실행을 굳이 하지 않아도 수정되는 부분이 자동적용,
# 서비스가 오픈된 이후는 사용자에게 완료되지 않은 개발과정을 공유하지 않기 위해 debug 모드 해제
app.run(port=3000, debug=True)

