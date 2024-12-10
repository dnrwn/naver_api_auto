import json

import GENERAL
import SCENARIO
from util import read

general_api_list = read.api_list('../api_data/general')
scenario_api_list = read.api_list('../api_data/scenario/image')
all_list = read.api_list('../api_data')


def a():
    for api_list_a in general_api_list:
        tc = GENERAL.GENERAL(api_list_a)
        tc.para_loop_2('invalid')
        # tc.test_test()
        # print(tc.header_i())
        # print(api_list_a)

        # tc.header_case()


def b():
    tc = GENERAL.GENERAL()
    # tc.test_test()
    tc.para_loop_2('valid')
    # tc.test_test_test()


def c():
    tc = SCENARIO.SCENARIO(scenario_api_list)
    tc.scenario_valid_case()


def json_file_write():
    for data_1 in all_list:
        data = read.api_data_read_info(data_1)
        print('0 : ', data_1)
        print('1 : ', data)
        print('2 : ', data[list(data)[1]])
        print('3 : ', list(data)[1])
        # if "info" in data and "category" in data["info"]:
        #     category = data['info']['category']
        #     print('2 : ', category)
        #     category_value = data["info"].pop("category")  # info에서 category 값 가져오고 삭제
        #     print('3 : ', category_value)
        #     print('4 : ', data[category])
        #     data[category]["category"] = category_value  # api_datalab_search 하위로 이동
        #
        # # 3. 새로운 파일로 저장
        if list(data)[1] in data:
            data['detail'] = data.pop(list(data)[1])
        with open(data_1, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # 파일 저장

        print(f"변경된 데이터가 '{data_1}' 파일에 저장되었습니다.")


a()
