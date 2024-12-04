import json


# JSON 파일 읽기
def json_data_read():
    with open('api_data/api_datalab.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def api_list(api_name, component_1, component_2, component_3):
    api = json_data_read()['api_list']
    return api[][api_name][component_1][component_2][component_3]


def api_info():
    pass

if __name__ == "__main__":
    api = json_data_read()['api_list']
    # api sample
    # api[API_NAME][COMPONENT_1][COMPONENT_2][COMPONENT_3]
    # - COMPONENT_1 : url, method, response_type, description, parameter, response
    # - COMPONENT_2 : parameter/response_name
    # - COMPONENT_3 : type, option, description
    for a in api:
        b = list(a.keys())[0]
        print(b)
        print("API 선택 \n", api[0][b])
        print("PARAMETER 선택 \n", api[0][b]['parameter'])
        print("parameter_name 선택 \n", api[0][b]['parameter']['startDate'])
        print("type 선택 \n", api[0][b]['parameter']['startDate']['type'])
