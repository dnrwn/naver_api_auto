import json

import requests

import item.item_1

test1 = item.item_1.test2

# API 정보
url = "https://openapi.naver.com/v1/datalab/search"
headers = {
    "Host": "openapi.naver.com",
    "User-Agent": "curl/7.49.1",
    "Accept": "*/*",
    "X-Naver-Client-Id": "uv_lv7I3jpwBqWkHVDOx",
    "X-Naver-Client-Secret": "2FttqJ6b99",
    "Content-Type": "application/json"
}

for key, group_name in {**test1["valid"], **test1["invalid"]}.items():
    # print(key)
    print(group_name)
    request_body = {
        "startDate": "2024-11-11",
        "endDate": "2024-11-11",
        "timeUnit": "month",
        "keywordGroups": [
            {
                "groupName": "A",
                "keywords": group_name
            }
        ],
        "device": "pc",
        "gender": "m",
        "ages": ["3"]
    }
    # API 요청 보내기
    response = requests.post(url, headers=headers, data=json.dumps(request_body))
    # print(response.json())
    if key in test1["valid"]:
        try:
            assert response.status_code == 200
            print('valid_pass')
        except AssertionError:
            print('fail')
        except Exception as e:
            print(f"Unexpected Error: {e}")

    elif key in test1["invalid"]:
        try:
            assert response.status_code == 400
            print('invalid_pass')
        except AssertionError:
            print('fail')
        except Exception as e:
            print(f"Unexpected Error: {e}")
