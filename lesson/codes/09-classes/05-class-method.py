class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        # class 메서드를 호출하는 class가 첫번째 인자로 들어오게 된다
        print(f'인구 수는 {cls.count}입니다.') # cls는 누구? => 여기선 모름(아직 number_of_population을 아무도 호출 X)
        # print(f'인구 수는 {Person.count}입니다.')
        # # class는 하위 클래스가 생길 수 있음. 하위 클래스가 갖다 쓰더라도 본인의 클래스를 컨트롤할 수 있도록 Person 사용 X 

person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population() # 이순간에 cls가 결정됨 -> Person이라는 클래스
