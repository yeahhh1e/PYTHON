import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])
# print(parsed_data['username'])
# print(parsed_data['company']['name'])

dummy_data=[]
id= 0
for user in parsed_data:
        user_id = user['id']
        name = user['name']
        if user_id <10:
            print(user_id)
            print(name)
            id+=1
        # parsed_data['id'] +=1
        print(parsed_data['name'])
for i in parsed_data:
    user_id = parsed_data['id']
    name = parsed_data['name']
for i in range(0,10):
    # print(parsed_data['id'])
    user_id = parsed_data['id'] + i
    print(user_id)
    user_name = None
    for user in parsed_data:
        if parsed_data['id'] == user_id:
            user_name = parsed_data['name']
            print(user_name)
            break
if user_name:
    print(user_name)
