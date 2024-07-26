def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2

result = make_sum(100, 30)
# print(result)
return_value = print(result) # 130 반환을 출력
print(return_value) # None  # print 함수는 return이 없다 출력만 되는거지 반환이 되는 것이 아님

print('----------------------------')

def my_func():
    print('hello, world') # 함수 안에 print 함수를 호출

result = my_func() # hello, world
print(result) # None

