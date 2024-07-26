# 클래스 정의
class Person: # 클래스는 속성과 메서드로 이루어져 있다
    blood_color = 'red' # blood_color는 속성

    def __init__(self, name): # 메서드
        self.name = name

    def singing(self):
        return f'{self.name}이 노래합니다.'
    
    
# 인스턴스 생성
singer1 = Person('iu')


# (인스턴스) 메서드 호출
print(singer1.singing())


# 속성(변수) 접근
print(singer1.blood_color)


# 인스턴스 속성(변수)
print(singer1.name) # 다른 인스턴스에는 없는 것 iu라는 인스턴스 변수는 singer1(본인)만이 쓸 수 있음