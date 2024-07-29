############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    i = 0
    n = 0
    # matrix를 순회하며 초기 설정 값 max 보다 크면 max 값을 해당 값으로 바꾼다
    for i in range(len(matrix)):
        for n in range(len(matrix[i])):
            total = 0
            a = matrix[i][n]
            if matrix[i-1][n] > 0:
               b = matrix[i-1][n]
            if matrix[i+1][n] > 0:
                c = matrix[i+1][n]
            if matrix[i][n+1] > 0:
                d = matrix[i][n+1]
            e = matrix[i][n-1]
            print(a,b,c,d,e)
    #         if total < new_total:
    #             total = new_total
    # return new_total
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
