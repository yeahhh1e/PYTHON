# 세트는 순서가 존재하지 않는다.
# add
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set) # {1, 2, 3, 4, 'a', 'c', 'b'} (순서 계속 바뀜)

my_set.add(4)
print(my_set) # {1, 2, 3, 'c', 'a', 4, 'b'} 중복이 되지 않음

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set) # set()

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set) # {1, 3, 'c', 'a', 'b'}
# my_set.remove(10) # KeyError: 10 없는 요소를 remove로 제거 X

# pop
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element)
print(my_set)

# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set) # {1, 3, 'a', 'c', 'b'}
print(my_set.discard(10)) # None

# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set) # {1, 2, 3, 'b', 4, 5, 'a', 'c'}

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4}
print(set1.intersection(set2)) # {1, 3}
print(set1.issubset(set2)) # False
print(set3.issubset(set1)) # True
print(set1.issuperset(set2)) # False
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9} 해쉬테이블에 저장된 순서로 나옴
                        # 정수는 순서대로 저장되는 이유?
                    

