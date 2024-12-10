import time

import requests

from util import read

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
class PARAMETER:
    def __init__(self, api_list_a='../api_data/datalab/api_datalab_search.json'):
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

    def para_loop(self, case_type):
        for query_a, query_b in self.item[self.para_info['query']][case_type].items():
            for display_a, display_b in self.item[self.para_info['display']][case_type].items():
                for startDate_a, startDate_b in self.item[self.para_info['startDate']][case_type].items():
                    for sort_a, sort_b in self.item[self.para_info['sort']][case_type].items():
                        self.request_body['query'] = query_b
                        self.request_body['display'] = display_b
                        self.request_body['startDate'] = startDate_b
                        self.request_body['sort'] = sort_b
                        print(self.request_body)
                        if self.api['method'] == 'GET':
                            response = requests.get(self.api['URL'], headers=headers['get'], params=self.request_body)
                        else:

                            response = requests.post(self.api['URL'], headers=headers['post'], json=self.request_body)
                        try:
                            assert response.status_code == 200
                            print(response.json())

                        except AssertionError:
                            print('error')
                            print(self.request_body)
                            print(response.json())

                        except Exception as e:
                            print(e)

                        time.sleep(0.1)
            #         self.__init__()
            #     self.__init__()
            # self.__init__()
