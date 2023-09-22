import pandas as pd
import requests
import xmltodict

def api_data(_url,_params):
    # 입력받은 주소와 데이터를 가지고 요청
    response = requests.get(_url, params=_params)
    # xml 데이터를 dict 형태로 변환
    data = xmltodict.parse(response.content)
    dict_data=data['response']['body']['items']['item']
    result = pd.DataFrame(dict_data)
    return result