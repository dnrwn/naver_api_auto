import json


# JSON 파일 읽기
def json_data_read():
    with open('data/api_list.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# input
def selector_category():
    return input('검색할 Category 입력\n-------------\n')


def selector_api_name():
    return input('선택할 API name 입력\n-------------\n')


def selector_key():
    return input('선택할 API의 Key 입력')


# output
def search_info():
    print("info")
    print("-------------")
    print(json_data_read()['info'])
    print("-------------")


def search_category_list():
    print("Category List")
    print("-------------")
    for rr in json_data_read()['item']:
        print(rr['category'])
    print("-------------")


def search_api_list():
    for rr in json_data_read()['item']:
        print(rr)


def search_category(tem=None):
    if len(tem) == 0:
        print("전체 검색")
    else:
        print("검색어 :", tem)
    print("-------------")

    for rr in json_data_read()['item']:
        if len(tem) == 0:
            return rr
        else:
            if rr['category'] == tem:
                return rr
    print("1-------------")


def search_api_name():
    return search_category(selector_category())['api_list'][selector_api_name()]


def search_key():
    return search_api_name()[selector_key()]


if __name__ == "__main__":
    search_info()
    search_category_list()
    search_api_list()
