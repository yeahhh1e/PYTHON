# 할당
# 가변 데이터
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]

# 불변 데이터
a = 20 # 불변 데이터 타입 int
b = a
b = 10

print(a) # 20 (불변) # 리스트도 방 주소는 바뀌지 않지만 그 안의 요소를 바꿀 수 있는 것
         # but 정수는 방에 있는 20이라는 값 자체를 바꿀 수 없음. 다른 방의 주소값을 바라볼 수 있도록 재할당을 하게 됨
print(b) # 10


# 얕은 복사
a = [1, 2, 3]
b = a[:]
c = a.copy()

b[0] = 100
c[0] = 999
print(a) # [1, 2, 3]
print(b) # [100, 2, 3] # b는 모습만 같을 뿐 a와 다른 주소
print(c) # [999, 2, 3]

# 얕은 복사의 한계
a = [1, 2, [3, 4, 5]]
b = a[:] # 첫번째 방까지는 복사가 되는데 그 다음([3, 4, 5])은 같은 주소를 바라보게 됨.
         # 첫번째는 다르고 뒤에는 같게 됨

b[0] = 999
b[2][1] = 100
print(a) # [1, 2, [3, 100, 5]]
print(b) # [999, 2, [3, 100, 5]]

# 깊은 복사
import copy # 내장모듈
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a) # 두번째도 다른 방을 갖게 됨.

b[2][1] = 100
print(a) # [1, 2, [3, 4, 5]]
print(b) # [1, 2, [3, 100, 5]]