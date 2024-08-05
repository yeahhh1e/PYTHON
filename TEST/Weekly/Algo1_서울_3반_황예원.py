import sys
sys.stdin = open("algo1_sample_in.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    number_list = []
    for _ in range(0, N):
        a = list(map(int, input().split()))
        number_list.append(a)

    max_sum = -999 # 음수 테스트케이스도 있으므로 최대값을 음수로 설정
    for i in range(len(number_list)):
        for j in range(len(number_list[0])):
            total = 0 # 미생물이 놓인 칸과 인접칸의 먹이양을 저장할 변수 설정
            for x, y in ((i, j), (i , j+1), (i+1, j), (i, j-1), (i-1, j)):
                if 0 <= x < len(number_list) and 0 <= y < len(number_list[0]):
                    total += number_list[x][y]  # 인덱스 범위 안의 칸만 total에 더해줌
            if max_sum < total: # total이 클 경우 max_sum의 값을 total 값으로 바꿔줌
                max_sum = total

    print(f'#{test_case} {max_sum}')

