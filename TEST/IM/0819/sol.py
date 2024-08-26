import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))
    x_list = [0]
    on_list = x_list + n_list   # 인덱스랑 번호 맞춰주기

    off_led = [0]*(N+1)
    cnt = 0  # 불켜는 횟수를 저장할 변수

    for i in range(1, N+1):
        if on_list[i] == 1 and off_led[i] == 0:   # 불을 켜줘야 된다면
            cnt += 1
            for j in range(1, N+1):
                if i*j < N+1 and off_led[i*j] == 0:  # 꺼져있으면 켜주기
                    off_led[i*j] = 1
                elif i*j < N+1 and off_led[i*j] == 1:   # 켜져있었으면 꺼주기
                    off_led[i*j] = 0
                elif on_list == off_led:
                    break
        elif on_list[i] == 0 and off_led[i] == 1: # 불을 꺼줘야 된다면
            cnt += 1
            for j in range(1, N + 1):
                if i*j < N+1 and off_led[i*j] == 1: # 켜져있었으면 꺼주기
                    off_led[i * j] = 0  # 불 꺼주기
                elif i*j < N+1 and off_led[i*j] == 0:  # 꺼져있었으면 켜주기
                    off_led[i*j] = 1
                elif on_list == off_led:
                    break
        elif on_list == off_led:
            break

    print(f'#{tc} {cnt}')