class Person:
    # 클래스 변수 count
    count = 0

    def __init__(self, name):
        # 인스턴스 변수 name
        self.name = name
        Person.count += 1

person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)  # 2

##########################

class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(c1.r)
print(c2.r) 


c1.pi # 먼저 c1 본인에게서 pi라는 변수가 있는지 참조함 -> 없음 -> 찾으러 class로 올라감 -> 3.14 출력
c1.pi = 100 # c1의 인스턴스 변수 pi를 생성

print(Circle.pi) # 3.14 pi는 클래스 변수이므로 클래스가 활용해야함(이것이 올바른 방법)
print(c1.pi) # 100
print(c2.pi) # 3.14


