import time

import requests

from util import read

client = {
    'client_id': 'uv_lv7I3jpwBqWkHVDOx',
    'client_secret': '2FttqJ6b99'
}

# response 정의
headers = {
    "get": {
        "Host": "openapi.naver.com",
        "User-Agent": "curl/7.49.1",
        "Accept": "*/*",
        "X-Naver-Client-Id": client['client_id'],
        "X-Naver-Client-Secret": client['client_secret']
    },
    "post": {
        "Host": "openapi.naver.com",
        "X-Naver-Client-Id": client['client_id'],
        "X-Naver-Client-Secret": client['client_secret'],
        "Content-Type": "application/json"
    }
}


## input
class GENERAL:
    def __init__(self, api_list_a):
        self.api = read.api_data_read(api_list_a)  # api data read
        self.item = read.test_item_read('../item/test_item.json')  # test item read

        self.para_info = self.para_info()
        self.request_body = self.para_init()

        self.para_item = list(self.para_info)

        self.headers = self.header_init()  # header test 용도

    def para_info(self):
        # api_data의 parameter value로 test item의 case 찾기
        # 반복문에 사용
        # {
        # parameter_1:string_1,
        # parameter_2:integer
        # }
        return {
            param: data['case']
            for param, data in self.api['parameter'].items()
            if data['case'] != ''
        }

    def para_init(self):
        # api_data의 parameter 옵션에 맞게 초기 data 생성
        # response 요소로 사용
        # {
        # parameter_1:'',
        # parameter_2:''
        # }

        return {
            param: list(self.item[data['case']]['valid'].values())[0]
            for param, data in self.api['parameter'].items()
            if data['case'] != '' and data['Mandatory/Optional'] == 'Mandatory'
        }

    def header_init(self):
        return headers

    def scenario_invalid_case(self):
        # scenario case 는 general script 로 invalid case 만 대응 가능 (key 값을 valid 로 넣을 필요가 없기 때문)
        for key_a in self.para_item:
            for _, para_v in self.item[self.para_info[key_a]]['invalid'].items():
                self.request_body[key_a] = para_v
                if self.api['method'] == 'GET':
                    response = requests.get(self.api['URL'], headers=headers['get'], params=self.request_body)
                else:

                    response = requests.post(self.api['URL'], headers=headers['post'], json=self.request_body)
                try:
                    assert response.status_code != 200

                    print('API : ', self.api['URL'])
                    print('pass_body : ', self.request_body)
                    print('pass_response : ', response.json())

                except AssertionError:
                    print('API : ', self.api['URL'])
                    print('fail_body : ', self.request_body)
                    print('fail_response : ', response.json())

                except Exception as e:
                    print('API : ', self.api['URL'])
                    print('error_body : ', self.request_body)
                    print('error_message : ', e)

                time.sleep(0.1)


class SCENARIO:
    def __init__(self, api_list_a):
        self.api = api_list_a

    def image_valid(self):
        # valid case 는 api 3개를 같이 활용 해야 함
        print(self.api)

    def audio_valid(self):
        pass

    def ClovaFaceRecognition_valid(self):
        pass
