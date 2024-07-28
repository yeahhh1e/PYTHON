number_of_people = 0


def increase_user():
    '''
    회원 수 증가 시켜주는 함수 ( 함수는 반환값이 없어도 된다 )
    '''
    global number_of_people
    number_of_people += 1

# 회원 가입과 기능상으로 동일한 로직
def create_user(name, age, address):
    print(f'현재 가입 된 유저 수 : {number_of_people}')

    user_info = {}
    user_info['name'] = name # 할당
    user_info['age'] = age # 할당
    user_info['address'] = address # 할당

    print(f'{name}님 환영합니다!')
    increase_user()
    
    return user_info
    # 회원 수 증가
    # return print(f'{name}님 환영합니다!')

# result = create_user() -> result 값을 추후 후가공
# print(result)
# print(f'{name}님 환영합니다!')
# print(create_user('홍길동', 30, '서울'))
a = create_user('홍길동', 30, '서울')
print(a)

print(f'현재 가입 된 유저 수 : {number_of_people}')