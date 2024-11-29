개요 : API Test를 자동화하기 위한 Tool 만들기

구조

1. 타겟 : Naver Open API 중 데이터랩, 검색 당 Sample 1개씩
- 구성 완료 후 추가 예정

2. 유지보수 관점에서 item 구분
- API data
- API data read
- Test item
- Result item
- Test Case
- Test Log

완료
1. API 문서에 있는 정보들을 Json 형태로 가공
- API 정보: name, URL, method, type, parameter, response
- Category로 API 묶음
- API 업데이트 시 info 부분 업데이트 필요
-

2. read.py : 정보 파싱 script 작성
- Category, API name, key 검색
- 검색한 key 의 value 출력
    - input 용도
    - output 용도

예정
1. Test item 설계
- type 별 Input 정리

2. Result item 설계
- assert 문 활용 방안

3. Test Case 작성
- for 문으로 최대한 간략하게

3. pytest 적용


