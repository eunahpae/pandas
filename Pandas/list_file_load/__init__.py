# 모듈을 폴더로 생성하는 경우, 파일이름을 '__init__.py'로 해야 해당폴더 실행시 자동으로 생성자명으로 되어있는 파일이 실행된다.
# (폴더가 아닌 파일로 생성하여 로드하는 경우는 파일이름은 자유롭게 작성가능)
# 폴더로 작성하는 이유는 필요한 함수들이 많을 경우 하나의 파일에 다 담기에는 코드가 너무 길어지기에 여러파일로 작성하게 되는 경우를 위함.
# 여러파일이 폴더에 들어있는 경우, 해당 파일들을  '__init__.py' 에 import 하여 기능을 호출, 결과를 되돌려주면 된다.


# 라이브러리 로드
import pandas as pd
import os


# 파일을 불러와서 결합하는 과정을 함수로 만들어 놓고, 필요시마다 함수를 호출하여 사용 

def list_data(_path, _end):
    # _path는 파일의 경로
    # 경로의 파일 목록 로드
    file_list = os.listdir(_path)
    
    # 특정한 확장자의 파일 목록을 만들기 위해 비어있는 리스트를 생성
    file_list2 = []
   
    for i in file_list:
        if i.split('.')[-1] == _end:
            file_list2.append(i) 
    
    # 함수의 결과값 -> 비어있는 데이터프레임
    result = pd.DataFrame()
    
    # 반복문을 이용하여 파일 목록들을 데이터프레임 로드하고 result 에 행결합
    for i in file_list2:
        # 로드하고자 하는 파일의 확장자가 다른경우 해당 조건에 맞게 실행되도록 if조건문 작성
        # _end 가 csv 라면 read_csv()
        # _end 가 json 라면 read_json()
        # _end 가 xlsx,xls 라면 read_excel()
        if _end =='csv':
            df =  pd.read_csv(_path+'/'+i)
        elif _end =='json':
            df =  pd.read_json(_path+'/'+i)
        elif _end in ['xlsx','xls']:
            df =  pd.read_excel(_path+'/'+i)
        else:
            return "지원하지 않는 확장자입니다."       
        # df = pd.read_csv(_path+'/'+i) # 혹시 경로에 마지막 '/'를 추가하지 않는 경우에도 오류가 발생하지 않도록 '/' 추가 ('/'가 2개여도 정상작동)
        result = pd.concat([result,df], axis=0)

    return result