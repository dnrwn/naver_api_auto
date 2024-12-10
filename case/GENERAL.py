import time

import requests

from util import read, result_file

# 접근 권한
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
    def __init__(self, api_list_a='../api_data/general/datalab/api_datalab_search.json'):
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

    def header_case(self):
        if self.api['method'] == 'GET':
            return requests.get(self.api['URL'], headers=self.headers['get'])
        elif self.api['method'] == 'POST':
            return requests.post(self.api['URL'], headers=self.headers['post'])

    def para_loop_2(self, case_type):
        for key_a in self.para_item:
            for _, para_v in self.item[self.para_info[key_a]][case_type].items():
                self.request_body[key_a] = para_v
                if self.api['method'] == 'GET':
                    response = requests.get(self.api['URL'], headers=headers['get'], params=self.request_body)
                else:

                    response = requests.post(self.api['URL'], headers=headers['post'], json=self.request_body)
                try:
                    if case_type == 'valid':
                        assert response.status_code == 200
                    elif case_type == 'invalid':
                        assert response.status_code != 200

                    result_file.result_file(
                        api_name=self.api['category'],
                        case_type=case_type,
                        result="PASS",
                        request_body=self.request_body,
                        response_data=response.json()
                    )

                except AssertionError:
                    result_file.result_file(
                        api_name=self.api['category'],
                        case_type=case_type,
                        result="FAIL",
                        request_body=self.request_body,
                        response_data=response.json()
                    )

                except Exception as e:
                    result_file.result_file(
                        api_name=self.api['category'],
                        case_type=case_type,
                        result="ERROR",
                        request_body=self.request_body,
                        error_message=str(e)
                    )

                time.sleep(0.1)  # 없으면 api 성능 제약으로 의도하지 않은 결과 출력

    def test_test_test(self):
        for param, data in self.api['parameter'].items():
            if data['Mandatory/Optional'] == 'Mandatory':
                self.request_body[param] = list(self.item[data['case']]['valid'].values())[0]
                print(self.request_body)
            else:
                self.request_body[param] = None

    def test_test(self):
        print('para_item : ', self.para_item)
        print('para_info : ', self.para_info)
        a = 0
        for key_a in self.para_item:
            for k in list(self.item[self.para_info[key_a]]['valid'].values()):
                pass
            print('items : ', list(self.item[self.para_info[key_a]]['valid'].values())[0])
            # a = a + 1
            #     print('item : ', k)
