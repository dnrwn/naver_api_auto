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

        self.headers = self.head_init()  # header test 용도


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

    def para_loop_2(self, case_type):
        for key_a in self.para_item:
            for _, para_v in self.item[self.para_info[key_a]][case_type].items():
                self.request_body[key_a] = para_v
                if self.api['method'] == 'GET':
                    response = requests.get(self.api['URL'], headers=headers['get'], params=self.request_body)
                else:

                    response = requests.post(self.api['URL'], headers=headers['post'], json=self.request_body)
                try:
                    assert response.status_code == 200
                    # print('pass_body : ', self.request_body)
                    # print('pass_response : ', response.json())

                except AssertionError:
                    print('fail_body : ', self.request_body)
                    print('fail_response : ', response.json())

                except Exception as e:
                    print('error : ', e)

                time.sleep(0.1)

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

    def head_init(self):
        return headers

    def header_case(self):
        if self.api['method'] == 'GET':
            return requests.get(self.api['URL'], headers=self.headers['get'])
        elif self.api['method'] == 'POST':
            return requests.post(self.api['URL'], headers=self.headers['post'])
