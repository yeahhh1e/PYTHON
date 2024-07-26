# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) # {}

# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country','Unknown')) # Unknown
# print(person['country']) # KeyError: 'country' key를 조회해서 error가 나오면 안 된다 -> get method
                         # 문제가 생기면 중단해야 된다 -> key로 조회

# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys()) # dict_keys(['name', 'age']) # 대괄호 -> 리스트형태 -> 반복으로 풀어낼 수 있다
for item in person.keys():
    print(item)

# values
person = {'name': 'Alice', 'age': 25}
print(person.values()) # dict_values(['Alice', 25])
for item in person.values():
    print(item) 

# items
person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)]) # 튜플 형태
for item in person.items():
    print(item) # ('name', 'Alice')
                # ('age', 25)

for key, value in person.items():
    print(key, value) # name Alice
                      # age 25 언패킹 돼서 나옴

# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age')) # 25 반환
print(person) # {'name': 'Alice'}
print(person.pop('country', None)) # None
# print(person.pop('country')) # KeyError: 'country'

# setdefault
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA')) # KOREA 반환
print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

person.update(age=100, country='KOREA')
print(person) # {'name': 'Jane', 'age': 100, 'gender': 'Female', 'country': 'KOREA'}

# a = {} a는 애초에 b와 다른 주소값을 가지고 있음
# b = {'name': 'Alice', 'age': 25}

# a.update(b)
# print(a) # {'name': 'Alice', 'age': 25}
# b['name'] = 'Harry'
# print(a) # {'name': 'Alice', 'age': 25}