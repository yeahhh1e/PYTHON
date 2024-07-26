# find
text = 'banana'
print(text.find('a')) # 1
print(text.find('z')) # -1 (찾는 값이 존재하지 않음)

# index
print(text.index('a')) # 1
# print(text.index('z')) # ValueError: substring not found

# isupper
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # True
print(string2.isupper()) # False (전체가 다 대문자가 아니므로)

# islower
string1 = 'HELLO'
string2 = 'Hello'
print(string1.islower()) # False 
print(string2.islower()) # False (전체가 다 소문자가 아니므로)

# isalpha
string1 = 'Hello'
string2 = '123dfjd923ksh'
print(string1.isalpha()) # True 
print(string2.isalpha()) # False (전체가 다 알파벳이 아니므로)

# replace (원본은 변하지 않고 새로운 문자열을 반환)
text = 'Hello, world! world world'
new_text = text.replace('world', 'Python', 1)
print(new_text) # Hello, Python! world world

# strip
text = '  Hello, world!  '
new_text = text.strip() # 인자 없으면 공백 제거해줌
print(new_text)

# split
text = 'Hello, world!'
words = text.split(',')
words2 = text.split() # 공백을 기준으로 나눠줌
print(words) # ['Hello', ' world!'] , 를 기준으롤 나눴기 때문에 ' world!'가 됨. world 앞에 공백
print(words2) # ['Hello,', 'world!']

# join
words = ['Hello', 'world!']
new_text = '-'.join(words)
new_text2 = ''.join(words)
new_text3 = ' '.join(words)
print(new_text) # Hello-world! 다시 문자열로 되돌렸음
print(new_text2) # Helloworld!
print(new_text3) # Hello world!

# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1) # Hello, world! 맨 앞에 대문자로 바꾸고 뒤에 모두 소문자로 변경

# title
new_text2 = text.title()
print(new_text2) # Hello, World! 뒤에 w를 대문자 처리

# upper
new_text3 = text.upper()
print(new_text3) # HELLO, WORLD

# lower
new_text3 = text.lower()
print(new_text3) # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5) # HEllO, WOrLD! 기존 대문자 -> 소문자. 대소문자 교체


# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal()) # 소수점 => 전부 F
print("'-123'.isdecimal():", '-123'.isdecimal()) # 음수 (-는 기호이므로) => 전부 F
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())
