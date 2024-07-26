class Person:
    def __init__(self, name):

        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        # -> 둘이 관련 없음 self.ssafy = name 도 가능
        self.name = name # 생성될 때 self 인스턴스의 name 이라는 변수를 넣으면서 생성
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요, {self.name}입니다.')

person1 = Person('지민')
person1.greeting() # 객체중심*person1 중심)
# Person.greeting(person1) # 실제로는 이런 식으로 구동되지만 위처럼 사용. 객체지향이므로