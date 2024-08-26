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
    for i in range(N): # A 부터 탐색하자
        min_sum = 99999  # 최소값을 저장할 변수
        for j in range(N):
            if min_sum > matrix[i][j] and i != j and check_list[i] != 1 and check_list[j] !=1:
                min_sum = matrix[i][j]
                min_i = i
                min_j = j
        total += min_sum
        check_list[i] = 1
        check_list[j] = 1
        # i-j순으로 세웠으니 j의 다음에 누가 올지를 탐색해야함
        min_sum = 99999
        for x in range(N):
            if min_sum > matrix[j][x] and j != x:
                min_sum = matrix[j][x]
        total += min_sum
        break

    print(f"#{tc} {total}")

