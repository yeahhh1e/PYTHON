import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())                            # 스위치 개수
    lights = list(map(int, input().split()))    # 불 켜진 스위치(입력 받은 것)
    switches = [0] * N                          # 불 꺼진 스위치(입력 받은 것과 비교)
    result = 0                                  # 최소 횟수

    for i in range(N):                          # 앞에서부터 탐색
        if lights[i] != switches[i]:            # 만약 두 리스트의 값이 다르면
            result += 1                         # 스위치 누름
            for j in range(i, N, i + 1):        # 해당 인덱스부터 해당 스위치의 배수마다 상태 변경
                switches[j] = 1 - switches[j]

    print(f'#{tc} {result}')
