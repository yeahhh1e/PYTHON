import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = [int(num) for num in input().split()]
    # print(data)
    ans = [0] * (N+1)
    # print(ans)
    cnt = 0

    for i in range(N):
        if data[i] != ans[i+1]:
            cnt += 1
            for a in range(N+1):
                if a % (i+1) == 0:
                    ans[a] = not ans[a]
    # print(cnt, *ans)


    print("#%d %d" % (test_case, cnt))