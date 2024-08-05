import sys
sys.stdin = open("sample.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    number_list = list(map(int, input().split()))

    a = len(number_list)

    # 리스트를 순회하며 오르막 구간 끊기
    new_list = []
    min_result = 99 # 우선 크게 설정
    max_long = 0

    for i in range(0, a):
        new_list.append(number_list[i])
        if i == a-1: # 인덱스 마지막이면 계산 후 for문 종료
            if new_list[-1] != new_list[0]:
                A = new_list[-1]
                B = new_list[0]
                C = len(new_list)
                result = float((A - B) / C)
                long = C
                new_list = []  # 리스트 초기화
                if min_result > result: # 오르막의 최소 길이가 2이상이어야 됨.. (여기서 틀림)
                    min_result = result
                    max_long = C
                elif min_result == result:
                    if max_long < C:  # 오르막 길이가 긴 경우만 min_result에 저장
                        min_result = result
                        max_long = C
                break
            else:
                A = new_list[-1]
                C = len(new_list)
                result = float(A / C)
                long = C
                new_list = []  # 리스트 초기화
                if min_result > result:
                    min_result = result
                    max_long = C
                elif min_result == result:
                    if max_long < C:  # 오르막 길이가 긴 경우만 min_result에 저장
                        min_result = result
                        max_long = C
                break

        elif number_list[i] <= number_list[i+1]:
            continue

        elif number_list[i] > number_list[i+1]:
            A = new_list[-1]
            B = new_list[0]
            C = len(new_list)
            result = float((A - B) / C)
            long = C
            new_list = [] # 리스트 초기화
            if min_result > result:
                min_result = result
                max_long = C
            elif min_result == result:
                if max_long < C:  # 오르막 길이가 긴 경우만 max_result에 저장
                    min_result = result
                    max_long = C
            else:
                continue

    print(f'#{test_case} {max_long}')
