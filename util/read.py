import json
import os


# JSON 파일 읽기
def api_data_read(api_info):
    # info 제외
    with open(f"{api_info}", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['detail']


def api_data_read_info(api_info):
    # info 포함
    with open(f"{api_info}", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def test_item_read(test_item):
    with open(f"{test_item}", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def api_list(path='../api_data/general'):
    a = os.walk(path)
    b = []
    for root, _, files in a:
        for file in files:
            if file.endswith('.json'):
                b.append(os.path.join(root, file))
                # print(os.path.join(root, file))
    return b


if __name__ == "__main__":
    # api sample
    # api[COMPONENT_1][COMPONENT_2][COMPONENT_3]
    # - COMPONENT_1 : URL, method, response_type, description, parameter, response
    # - COMPONENT_2 : parameter/response_name
    # - COMPONENT_3 : type, Mandatory/Optional, description

    # api = api_data_read('../api_data/datalab/api_datalab_search.json')
    # print("API 정보 \n", api)
    # print("PARAMETER 선택 \n", api['parameter'])
    # print("parameter_name 선택 \n", api['parameter']['key'])
    # print("type 선택 \n", api['parameter']['key']['type'])
    #
    # # test item sample
    # # item[COMPONENT_1][COMPONENT_2][COMPONENT_3]
    # # - COMPONENT_1 : Item ID
    # # - COMPONENT_2 : valid/invalid
    # # - COMPONENT_3 : Case
    # file = '../item/test_item.json'
    # item = test_item_read(file)
    # print("Item 정보 \n", item['string_1']['valid'])
    # for a in item['string_1']['valid']:
    #     print(item['string_1']['valid'][a])

    # api_list sample
    print(api_list())
