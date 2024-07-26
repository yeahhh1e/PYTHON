# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Yewon', 20)
greet(20, 'Yewon') # 매개변수에 의미가 있는 것은 아니므로 실행 됨
# greet('Yewon') # TypeError: greet() missing 1 required positional argument: 'age'


# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')
greet('Charlie', 40)

# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)
greet(age=35, name='Dave') # 키워드 인자로 넣었으므로 실행 됨
# greet(age=35, 'Dave') # 안 됨

# 4. Arbitrary Argument Lists
def calculate_sum(params, *args): # args는 매개변수의 이름일 뿐
    print(args)
    print(type(args))

calculate_sum(1, 100, 5000, 30) # (1, 100, 5000, 30) 튜플 1이 paramsr가 됨



# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30)

# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')


print('--------')
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')

calculate_sum(1,2,3)
