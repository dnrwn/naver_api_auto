import json


# JSON 파일 읽기
def json_data_read():
    with open('data/api_list.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def search_api_list(cate):
    for depth_1 in json_data_read()['item']:
        if depth_1['category'] == cate:
            return depth_1['api_list']

if __name__ == "__main__":
    # api data 조회 예시
    # search_api_list(Category)[api_name][1depth_key_name].key()
    # 1depth_key_name = URL, method, response type, parameter, response
    # search_api_list(Category)[api_name][1depth_key_name][2depth_key_name].key()
    # 2depth_key_name = parameter / response list
    # parameter : name
    # response : name
    # search_api_list(Category)[api_name][1depth_key_name][2depth_key_name][3depth_key_name].key()
    # 3depth_key_name = parameter / Response data
    # parameter : type, option
    # response : type
    print(search_api_list('검색')['api_1']['parameter'].keys())
    print(search_api_list('검색')['api_1']['parameter']['query'].keys())
    print(search_api_list('검색')['api_1']['parameter']['query']['type'])
