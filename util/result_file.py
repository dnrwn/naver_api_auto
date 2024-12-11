import json
import os
from datetime import datetime


def result_file(api_name, case_type, result, request_body, response_data=None, error_message=None, header=None):
    # 파일 생성 경로
    date_1 = datetime.now().strftime('%Y%m%d')
    path = f"../result/{date_1}/{api_name}/{result}"
    try:
        os.makedirs(path)
    except:
        pass
    # 파일 생성 규칙
    date_2 = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = f"{api_name}_{case_type}_{result}_{date_2}.json"
    data = {
        "api_name": api_name,
        "result": result
    }
    if header:
        data['header'] = header
    if response_data:  # 응답 데이터가 있으면 추가
        data["response"] = response_data
        data["parameter"] = request_body
    if error_message:  # 에러 메시지가 있으면 추가
        data["error_message"] = error_message
        data["parameter"] = request_body

    with open(f"{path}/{filename}", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
