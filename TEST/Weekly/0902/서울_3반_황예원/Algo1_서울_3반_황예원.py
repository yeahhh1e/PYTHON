T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input()))

    max_len = 0
    for i in range(N):
        if i == 0 or i == 1:  # 첫번째와 두번째는 어차피 대칭구간 길이 안 되므로 검사 패스
            pass
        else:
            center = i//2   # 중심 찾기
            len_v = 0
            for j in range(1, center+1): # 중심까지의 거리만큼 양 옆 탐색
                if j == 1: # 양 옆 하나만 탐색할 때
                    left = n_list[center-1]
                    right = n_list[center+1]
                else: # 두 개 탐색할 때
                    left_list = n_list[center-j:center] # 왼쪽으로 j만큼 담기
                    left = []
                    for x in range(len(left_list)-1, -1, -1):  # 마지막부터 첫 인덱스까지 거꾸로 순회하며 left에 담기
                        left.append(left_list[x])
                right = list(n_list[center + 1: center + j + 1])  # right는 중심값 다음부터 j까지 list로 담기

                if left == right:   # 왼쪽 오른쪽 비교
                    len_v = len(n_list[center-j:center+j+1]) # 중심값 기준 양옆 j만큼의 길이 구하기
                else: # 같지 않으면
                    len_v = 1
                if max_len < len_v:
                    max_len = len_v

    print(f"#{tc} {max_len}")