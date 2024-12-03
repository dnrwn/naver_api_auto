import json


def json_data_read():
    with open('api_data/api_search.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['item']


def read_json_to_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # JSON 데이터를 사전으로 변환
    return data


if __name__ == "__main__":
    file_path = 'api_data/api_search.json'  # JSON 파일의 경로
    print(type(json_data_read()))  # 변환된 dict 출력

    print(type(read_json_to_dict(file_path)))
