import math

##############################
# 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
#
# 모든 수신값은 gameData에 들어갑니다.
#   - gameData.order: 1인 경우 선공, 2인 경우 후공을 의미
#   - gameData.balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
#     예) gameData.balls[0][0]: 흰 공의 X좌표
#         gameData.balls[0][1]: 흰 공의 Y좌표
#         gameData.balls[1][0]: 1번 공의 X좌표
#         gameData.balls[4][0]: 4번 공의 X좌표
#         gameData.balls[5][0]: 마지막 번호(8번) 공의 X좌표

# 여기서부터 코드를 작성하세요.
# 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

# Vector 구현
class Vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f'{self.x:.10f}, {self.y:.10f}'

    @property
    def _comp(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vector(*(i + j for i, j in zip(self._comp, other._comp)))

## 벡터의 크기: norm
    @property
    def norm(self):
        return sum(i * i for i in self._comp) ** (1 / 2)


# 벡터의 내적: dot // 두 벡터 사이의 각도 계산
# 양수면 같은 방향 / 음수면 반대 방향
    def dot(self, other):
        return sum(i * j for i, j in zip(self._comp, other._comp))

# 벡터의 외적: cross // 두 벡터가 평면에서 얼마나 회전했는지
# 0이면 두 벡터는 평행
    def cross(self, other):
        return (self.x * other.y - self.y * other.x)

    def __neg__(self):
        return Vector(*(-i for i in self._comp))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.cross(other)
        return Vector(*(other * i for i in self._comp))

    def __rmul__(self, other):
        if isinstance(other, Vector):
            return self.cross(other)
        else:
            return self.__mul__(other)

    def __truediv__(self, other):
        return Vector(*(i / other for i in self._comp))

## 경로 찾기 함수
# x 부터 y까지 가는 경로 계산하는 함수 (두 점 사이의 경로 계산)
# 경로 가는 동안 다른 공들과 충돌하지 않는지 확인하는게 핵심
# 단순하게 >> ((y: Vector - x: Vector))
def path_find(x: Vector, y: Vector):

    ## 경로 상에 다른 공이 있는지 검사
    def path_check(path: Vector, start, end):
        checkvec = end - start
        checkvec = checkvec / checkvec.norm
        cnt = 0
        for ball in objball + enemyball + [myball] + Myholes:
            checkball = ball - start
            # dot : 공이 경로 상에 있는지 확인
            if checkvec.dot(checkball) < 0:
                continue
            # cross : 공이 실제로 경로에 얼마나 가까이 있는 지를 판단
            if abs(checkvec.cross(checkball)) < 1.5 * Ball_r:
                cnt += 1
            # print(cnt)
        print(start, end, cnt)
        # 만약 특정 경로에서 두 개 이상의 공이 경로를 방해하면,
        # 그 경로는 유효하지 않다고 판단
        if cnt > 2:
            return False
        return True

    path = y - x
    if path_check(path, x, y):
        return path
    return None


Ball_stack = []
Ball_r = 5.73 / 2
Ball_R = 5.73
W = 254
H = 127
# 일부러 홀의 위치를 보이기보다 약간 안쪽으로 잡아당겨줌
# HOLES = [[0+Ball_r/4, 0+Ball_r/4], [127, 0+Ball_r/3], [254-Ball_r/4, 0+Ball_r/4], [0+Ball_r/4, 127-Ball_r/4], [127, 127-Ball_r/3], [254-Ball_r/4, 127-Ball_r/4]]

const = 0.3
k = Ball_r * const
print(k)
HOLES = [[0 + k, 0 + k], [127, 0 + k / 2], [254 - k, 0 + k], [0 + k, 127 - k], [127, 127 - k / 2], [254 - k, 127 - k]]
Myholes = []
for hole in HOLES:
    Myholes.append(Vector(*hole))
    # 홀 위치를 더 추가해서 정확도를 올리려했으나 실패?
    # for _ in range(20):
    #     seta = _*2*math.pi/20
    #     addvector = Vector(math.cos(seta),math.sin(seta))*Ball_r/10
    #     addvector = addvector/(2)
    #     Myholes.append(Vector(*hole) + addvector)

# for

# 내공
myball = Vector(*gameData.balls[0])
# 목적구
objball = []
# 상대구
enemyball = []

print(myball)
# 공을 정리함 -> 목적구 2개가 안넣어졌으면 8볼은 상대목적구로 봄
flag1 = False
flag2 = False
if gameData.order == 1:
    for idx, ball in enumerate(gameData.balls[1:]):
        # 목적구 2개가 다 끝났으면 True
        if ball == [-1.0, -1.0]:
            if idx == 0:
                flag1 = True
            if idx == 2:
                flag2 = True
            continue
        else:
            if idx == 0 or idx == 2:
                objball.append(Vector(*ball))
            elif idx == 1 or idx == 3:
                enemyball.append(Vector(*ball))
            elif idx == 4:
                if flag1 and flag2:
                    objball.append(Vector(*ball))
                else:
                    enemyball.append(Vector(*ball))
        # print(flag1,flag2)
else:
    for idx, ball in enumerate(gameData.balls[1:]):
        # 목적구 2개가 다 끝났으면 True
        if ball == [-1.0, -1.0]:
            if idx == 1:
                flag1 = True
            if idx == 3:
                flag2 = True
            continue
        else:
            if idx == 1 or idx == 3:
                objball.append(Vector(*ball))
            elif idx == 0 or idx == 2:
                enemyball.append(Vector(*ball))
            elif idx == 4:
                if flag1 and flag2:
                    objball.append(Vector(*ball))
                else:
                    enemyball.append(Vector(*ball))
        # print(flag1,flag2)

# print(myball)
# print(objball)
# print(enemyball)

Pathlist = []

## 경로를 찾고 최적의 경로 선택
# 내 목적구에 대해서만
for obj in objball:
    cand_path = []
    # 모든 홀에 대해서
    for hole in Myholes:
        # obj이 hole에 가는 방법
        objtohole = path_find(obj, hole)
        if not objtohole:
            print('not objtohole pass')
            continue
        # objtohole을 위해 수구의 도착 위치 계산
        objtohole_nv = objtohole / (objtohole.norm)
        que = obj + Ball_R * -objtohole_nv
        # 수구 to que점을 가는 길 계산
        quetoobj = path_find(myball, que)
        if not quetoobj:
            print('no quetoobj pass')
            continue
        quetoobj_nv = quetoobj / (quetoobj.norm)
        # 두 백터의 각도 계산 (단위백터끼리의 내적)
        # 영보다 작거나 음수면 안하고 진행
        if objtohole_nv.dot(quetoobj_nv) <= 0:
            continue
        # weights *= objtohole_nv.dot(quetoobj_nv)

        # 예측 힘의 값, objtohole 거리, quetoobj 거리에 비례하게 함

        mue = 5.5
        v1h = (55 + 2 * mue * objtohole.norm)
        v01 = (v1h + 2 * mue * quetoobj.norm) ** (1 / 2)
        inferF = quetoobj_nv * v01
        # 앞선 각도를 계산한 내적 값을 나눠주어 각도가 얇다면 더 쎄게 치도록 함
        inferF = inferF / (objtohole_nv.dot(quetoobj_nv) ** (1 / 2))
        # 완성된 패스를 등록
        cand_path.append([int(objtohole_nv.dot(quetoobj_nv) * 10), inferF.norm, inferF])

    cand_path.sort(key=lambda x: (-x[0], x[1]))
    if cand_path:
        Pathlist.append(cand_path[0])

# 가장 일직선으로 만나는 것 + 다음으로 힘의 필요가 가장 작은 것을 쓰자
Pathlist.sort(key=lambda x: (-x[0], x[1]))
print(Pathlist) # 최적의 경로


# 백터로 계산한 힘을 `힘`과 `각도`로 변환해줌
def Fchange(Pathnorm, Path: Vector):
    forcal = Path / (Pathnorm)

    # 백터 각도 계산
    # asin : 라디안으로 변환 (-pi/2~pi/2  사이)
    if forcal.x >= 0 and forcal.y >= 0:
        seta = math.asin(Vector(1, 0).cross(forcal))

    elif forcal.x <= 0 and forcal.y >= 0:
        seta = math.asin(Vector(0, 1).cross(forcal)) + math.pi / 2

    elif forcal.x <= 0 and forcal.y <= 0:
        seta = math.asin(Vector(-1, 0).cross(forcal)) + math.pi

    else:
        seta = math.asin(Vector(0, -1).cross(forcal)) + 3 * math.pi / 2

    # 힘 조정 (숫자 높이면 세게 침)
    weight1 = 0.42 # 경로의 길이에 비례한 힘의 가중치
    weight2 = 20 # 기본 힘

    print('weight1', (Pathnorm * weight1) / (Pathnorm * weight1 + weight2), 'weight2',
          (weight2) / (Pathnorm * weight1 + weight2))

    # 힘의 크기 계산
    F = Pathnorm * weight1 + weight2 # 최종 힘 크기

    # 각도 (0~360)
    # 라디안을 degree로 변환해야 실제 각도 얻기 가능
    degree = seta * 180 / math.pi
    degree = ((90 - degree) + 360) % 360
    if F > 100:
        F = 100
    return F, degree


# 만약에 하나도 없으면
# 경로가 없을 때 임의로 공을 침
if not Pathlist:
    tmp_list = []
    for obj in objball:
        tmp = path_find(myball, obj)
        if not tmp:
            continue
        tmp.x *= 1.001 # x축 방향 벡터 변환
        tmp.y *= 1.001 # y축 방향 벡터 변환
        tmp_list.append([tmp.norm, tmp])

    if not tmp_list:
        for obj in enemyball:
            temp = myball - obj
            temp.x = 1.5 * temp.x
            power, angle = Fchange(temp.norm, temp)
            break
    else:
        tmp_list.sort()
        power, angle = Fchange(*tmp_list[0])
        power = 80 # 힘의 강도 조정가능 / 기본 힘 설정

# 경로가 존재할 경우
else:
#  x[0]은 가중치(직선도)이고 x[1]은 힘의 필요
    # Pathlist = [[가중치1:각도, 가중치2:Norm, F백터]  ]
    power, angle = Fchange(*Pathlist[0][1:])

"""
# 조건을 추가하여 힘을 조정
# 공이 상대적으로 가까운 경우 더 강하게 치게 설정
if power < 50:
    power += 20  # 힘을 20 증가
else:
    power += 10  # 힘을 10 증가

# 각도를 일정 범위로 조정
angle = angle % 360  # 각도를 0-360 범위로 조정
"""

"""
# 힘과 각도 조정
power *= 1.1  # 힘을 10% 증가
angle += 5    # 각도를 5도 증가

# 각도가 360을 초과하지 않도록 조정
if angle >= 360:
    angle -= 360
"""

## 최종 출력부분
# conn.send(angle, power)
print(f'Power: {power}, Angle: {angle}')