# import sys
# sys.stdin = open("algo1_sample_in.txt","r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    f_list = list(map(int, input().split()))


    zero = [0]
    food_list = zero + f_list # 인덱스와 칸 순서 맞춰주기위해 앞에 0 추가

    result = False  # 최대 위치로 이동 했는지 확인하는 변수 설정
    now = 1  # 현재 위치
    while now < N+1:
        for i in range(1, K+1):
            check = False   # 먹이를 먹었는지 체크하는 변수 설정
            if now + i <= N and food_list[now + i] == 1:
                now += i # 먹이를 찾다가 발견하면 해당 위치로 이동한다.
                check = True
                if now == N:    # 구간의 끝에 도착하면 종료
                    result = True
                    break
                if now > N: # 구간보다 멀리가면 구간 끝으로 위치를 바꾸고 종료
                    now = N
                    result = True
                    break
        if check == False:  # 먹이를 못 찾았다면 K만큼 이동하고 구간 끝보다 멀리가면 위치 바꾸고 종료
            now += K
            result = True
            if now > N:
                now = N
                result = True
                break
            break

    print(f"#{tc} {now}")
