number_of_people = 0
number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

for i in name:
    print(f'{i}님 환영합니다!')

def create_user(name, age, address):
    global info
    info = {}
    info['name'] = name
    info['age'] = age
    info['address'] = address

    increase_user()
    decrease_book()

many_user = list(map(lambda n, a, ad: {'name':n, 'age':a, 'address':ad}, name, age, address))
# {'name': '김시습', 'age': 20, 'address': '서울'}
info = list(map(lambda user: {'name' : user['name'], 'age' : user['age']}, many_user))
# print(info)

    
def rental_book(info):
    decrease_book(info['age']//10)
    print(f"{info['name']}님이 {info['age']//10}권의 책을 대여하였습니다.")
# {'name': '김시습', 'age': 20}
list(map(rental_book, info))
