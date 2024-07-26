# 원주율
pie = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
circle = 15

circle_1 = '원주율 : '
circle_2 = '반지름 : '
circle_3 = '원의 둘레 : '
circle_4 = '원의 넓이 : '

circle_3_s = circle*2*pie
circle_4_s = circle**2*pie

print(f'{circle_1}{pie}')
print(f'{circle_2}{circle}')
print(circle_3,circle_3_s)
print(circle_4,circle_4_s)
