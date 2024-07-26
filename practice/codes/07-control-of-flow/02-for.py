items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)

country = 'Korea'

for char in country:
    print(char)

for i in range(5):
    print(i)

print(range(5)) # range(0, 5) range 자체도 시퀀스 

my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key) # x y z (키가 나옴)
    print(my_dict[key])


numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)): #len(numbers) = 5 -> 4까지 돌게 됨
    numbers[i] *= 2

print(numbers)

outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
'''
A c
A d
B c
B d
'''

elements = [
    ['A', 'B'], 
    ['c', 'd']
]

for elem in elements:
    for item in elem:
        print(item)

'''
A
B
c
d
'''