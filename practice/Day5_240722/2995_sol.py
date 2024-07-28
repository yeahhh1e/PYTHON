N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.

# 방법 1
print('방법1')
def insert(data):
    global arr_1
    for char in data:
        arr_1.append(char)
    return arr_1
insert(data_1)
print(arr_1)

# 방법 2
print('방법2')
arr_1 = list(data_1)
print(arr_1)



M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.

# 방법 1 
result = data_2.split(' ')
for i in result:
    if int(i) % 2 == 1:
        print(i)