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
        "Host": "openapi.naver.com",
        "X-Naver-Client-Id": client['client_id'],
        "X-Naver-Client-Secret": client['client_secret']
}

## input
class GENERAL:
    def __init__(self, api_list_a='../api_data/general/search/api_search_adult.json'):
        self.api = read.api_data_read(api_list_a)  # api data read
        self.item = read.test_item_read('../item/test_item.json')  # test item read
        self.para_info = self.para_info()
        self.request_body = self.para_init()
        self.para_item = list(self.para_info)
        self.headers = self.header_init()  # header test 용도

    def header_init(self):
        return headers.copy()

    def header_loop(self, case_type='header'):
        for key_a in self.para_item:
            for _, para_v in self.item[self.para_info[key_a]]['valid'].items():
                self.request_body[key_a] = para_v
        for header_r in self.headers:
            for _, header_a in self.item['header'].items():
                if header_r != 'Host':  # Host의 경우 header key만 있으면 pass로 동작함
                    self.headers[header_r] = header_a
                    if self.api['method'] == 'GET':
                        # GET 사용 시 params로 쿼리 data 전달
                        response = requests.get(self.api['URL'], headers=self.headers, params=self.request_body)
                    else:
                        # POST 사용 시 json으로 data 전달
                        response = requests.post(self.api['URL'], headers=self.headers, json=self.request_body)
                    self.result(case_type, response)
                self.headers = self.header_init()

    def para_info(self):
        # api_data의 parameter value로 test item의 case 찾기
        # test item에서 response에 삽입할 value를 찾는 용도로 사용
        # {parameter_1:string_1,parameter_2:integer}
        return {
            param: data['case']
            for param, data in self.api['parameter'].items()
            if data['case'] != ''
        }

    def para_init(self):
        # api_data의 parameter 초기 data 생성
        # response 요소로 사용
        # {parameter_1:'',parameter_2:''}
        return {
            param: list(self.item[data['case']]['valid'].values())[0]
            for param, data in self.api['parameter'].items()
            if data['case'] != '' and data['Mandatory/Optional'] == 'Mandatory'
        }

    def para_loop_2(self, case_type):
        for key_a in self.para_item:
            for _, para_v in self.item[self.para_info[key_a]][case_type].items():
                self.request_body[key_a] = para_v
                if self.api['method'] == 'GET':
                    # GET 사용 시 params로 쿼리 data 전달
                    response = requests.get(self.api['URL'], headers=headers, params=self.request_body)
                else:
                    # POST 사용 시 json으로 data 전달
                    response = requests.post(self.api['URL'], headers=headers, json=self.request_body)
                self.result(case_type, response)

    def result(self, case_type, response):
        time.sleep(1)  # 없으면 api 성능 제약으로 의도하지 않은 결과 출력 or 결과 수집 덮어써짐
        try:
            if case_type == 'valid':
                assert response.status_code == 200
            elif case_type == 'invalid':
                assert response.status_code != 200
            elif case_type == 'header':
                assert response.status_code == 401

            result_file.result_file(
                api_name=self.api['category'],
                case_type=case_type,
                header=self.headers,
                result="PASS",
                request_body=self.request_body,
                response_data=response.json()
            )
        except AssertionError:
            result_file.result_file(
                api_name=self.api['category'],
                case_type=case_type,
                header=self.headers,
                result="FAIL",
                request_body=self.request_body,
                response_data=response.json()
            )
        except Exception as e:
            result_file.result_file(
                api_name=self.api['category'],
                case_type=case_type,
                header=self.headers,
                result="ERROR",
                request_body=self.request_body,
                error_message=str(e)
            )
