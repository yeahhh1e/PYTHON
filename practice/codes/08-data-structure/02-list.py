# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
print(my_list.append(4)) # None append는 반환이 없음 원본을 바꾸기 때문에.

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]
# my_list.extend(5) 
# print(my_list) # TypeError: 'int' object is not iterable 
my_list.extend([5])
print(my_list) # [1, 2, 3, 4, 5, 6, 5]
my_list.append([9, 9, 9])
print(my_list) # [1, 2, 3, 4, 5, 6, [9, 9, 9]] 리스트 안에 리스트 자체를 넣으려면
               #append(인자를 하나만 받을 수 있음)를 사용

# insert
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list) # [1, 5, 2, 3]

# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list) # [1, 3, 2, 2, 2] 앞에 2만 지워짐

# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # 5
print(item2) # 1
print(my_list) # [2, 3, 4]

# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # []

# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index) # 1 # 2가 첫번째에 있음

# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number) # 3 (3이 세 개)

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list.reverse()) # None # reverse 메서드의 반환값이 없으므로 None 반환(원본을 뒤집었기 때문에 새로운 리스트 반환 x)
print(my_list) # [9, 1, 8, 2, 3, 1]

# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list) # [1, 2, 3, 100] (원본 변경)


# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list) # [100, 3, 2, 1] 내림차순으로 변경됨