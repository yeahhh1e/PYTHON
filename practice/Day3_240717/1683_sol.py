number_of_people = 0


def increase_user():
    '''
    회원 수 증가 시켜주는 함수 ( 함수는 반환값이 없어도 된다 )
    '''
    global number_of_people
    number_of_people += 1

# 회원 가입과 기능상으로 동일한 로직
def create_user(name, age, address):

    user_info = {}
    user_info['name'] = name # 할당
    user_info['age'] = age # 할당
    user_info['address'] = address # 할당

    increase_user()
    
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

for i in name:
    print(f'{i}님 환영합니다!')

many_user = list(map(create_user, name, age, address))
# print(many_user)   

# zip 함수 -> 얻다 씀 ?

# many_user = []
# for i in len(many_user):
#     many_user.append(create_user)

# List Comprehension
many_user = [create_user(n, a, ad) for n, a, ad in zip(name, age, address)]
print(many_user)



