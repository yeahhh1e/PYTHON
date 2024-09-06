import sys
sys.stdin = open("algo2_sample_in2.txt","r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    total = 0 # 위험도의 합계 저장할 변수
    min_i = 0
    min_j = 0
    check_list = [0]*N # 줄을 섰는지 체크하는 리스트

    def find_min(matrix):
        global total
        global min_i
        global min_j
        global i
        global j

        for i in range(N):
            min_sum = 99999
            for j in range(N):
                if check_list[j] != 1 and min_sum > matrix[i][j] and i != j:
                    min_sum = matrix[i][j]
                    min_i = i
                    min_j = j
            if min_sum != 99999:
                check_list[min_i] = 1
                check_list[min_j] = 1
                total += min_sum
        return total

    while check_list != [1]*N:
        find_min(matrix)

    print(f"#{tc} {total}")

