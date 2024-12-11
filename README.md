# 개요
API Test를 자동화하기 위한 script 작성 절차 정리

---
# 요약
json 형태의 data를 이용하여 최소의 함수로 모든 case를 실행하도록 대응하고 실행 결과 파일을 json 형태로 저장


---
# 상세
1. 타겟 설정 : NAVER openapi 항목
	1. 1단계 : 비로그인 방식 오픈 API
 	2. 2단계 : 로그인 방식 오픈 API

2. 요구사항
	1. 데이터랩
    	- 검색어 트렌드, 쇼핑 인사이트
	2. 검색
    	- 뉴스, 백과사전블로그, 쇼핑, 웹, 이미지 검색, 전문정보, 지식in, 책, 카페, 성인, 한영 오류 변환 검색, 업체 상호 검색
	4. 이미지 캡차 (시나리오)
	5. 음성 캡차 (시나리오)
	6. 네이버 공유하기 (web UI 기반 기능)
	7. 네이버 오픈메인 (Mobile web UI 기반 기능)
	8. Clova Face Recognition (시나리오)

3. Excel에 요구사항 정리 (../doc/naver_open_api_정리_통합_1210.xlsx)
	1. 개요 : API 개요 정리 (API Name, API sub Name, 요구사항 Link)
	2. API Info : API Name, 요청 URL, Method, Response_Type 정보 정리
	3. 통합 : API Name, Component (Parameter, Response, Error), Name, Type, Mandatory/Optional, Description 정보 정리
	4. Header : Header 정보 정리

4. Excel에 Input Case 설계 (../doc/naver_open_api_정리_통합_1210.xlsx)
	1. Parameter Type 별 Case 설계
		- string, Array, Integer, Mandatory/Optional
	2. Header Case 설계

5. Excel에 정리한 요구사항 정보를 Json data로 정리 (../api_data/.../....json)
	- general : 데이터랩, 검색
	- scenario : 이미지 캡차, 음성 캡차, Clova Face Recognition

6. Excel에 정리한 Input Case 정보를 Json data로 정리 (../item/test_item.json)

7. json 파일 read 코드 작성 (../util/read.py)

8. Json data의 API Info와 Test Item을 이용한 requests 전송 script 작성 (../case/GENERAL.py)

9. requests 실행 결과 파일을 json 형태로 생성하는 script 작성 (../util/result_file.py)
	- ../result/yyyymmdd/실행결과/apiname_(valid/invalid)_실행결과_실행날짜시간.json

10. script 실행 script 작성 (../case/run.py)

---
# 결과
생성 경로 : ..\result\20241212\api_search_adult\PASS\api_search_adult_header_PASS_20241212-014213.json
```json
{
    "api_name": "api_search_adult",
    "result": "PASS",
    "header": {
        "Host": "openapi.naver.com",
        "X-Naver-Client-Id": "uv_lv7I3jpwBqWkHVDOx",
        "X-Naver-Client-Secret": null
    },
    "response": {
        "errorMessage": "Not Exist Client Secret : Authentication failed. (인증에 실패했습니다.)",
        "errorCode": "024"
    },
    "parameter": {
        "query": "abc",
        "display": 100,
        "startDate": 1000,
        "sort": "date"
    }
}
