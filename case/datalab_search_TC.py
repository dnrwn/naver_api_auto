import requests
import time

from util import read

# 접근 권한
client_id = 'uv_lv7I3jpwBqWkHVDOx'
client_secret = '2FttqJ6b99'

# response 정의
headers = {
    "Host": "openapi.naver.com",
    "User-Agent": "curl/7.49.1",
    "Accept": "*/*",
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}


## input
class PARAMETER:
    def __init__(self, api_list_a):
        print(api_list_a)
        self.api = read.api_data_read(api_list_a)
        print(self.api)
        self.item = read.test_item_read('../item/test_item.json')

        self.para_info = self.para_info()  # for 문에 사용
        self.request_body = self.para_init()  # parameter 삽입에 사용

        self.para_item = list(self.para_info)

    def para_info(self):
        return {param: data['case'] for param, data in self.api['parameter'].items()}

    def para_init(self):
        return {param: "" for param, data in self.api['parameter'].items()}

    def para_loop_2(self, case_type):
        for key_a in self.para_item:
            for para_k, para_v in self.item[self.para_info[key_a]][case_type].items():
                self.request_body[key_a] = para_v
                print(self.request_body)
                response = requests.get(self.api['URL'], headers=headers, params=self.request_body)
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
                        response = requests.get(self.api['URL'], headers=headers, params=self.request_body)
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
