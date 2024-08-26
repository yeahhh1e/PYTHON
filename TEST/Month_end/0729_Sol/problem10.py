############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    i = 0
    n = 0
    max = matrix[0][0]

    # matrix를 순회하며 초기 설정 값 max 보다 크면 max 값을 해당 값으로 바꾼다
    for i in range(len(matrix)):
        for n in range(len(matrix[i])):
            if matrix[i][n] > max:
                max = matrix[i][n]

    # 빈 리스트를 만든다
    lst = []

    # 다시 matrix를 순회하며 아까 저장한 max값과 같은 값을 가진 matrix의 인덱스를 찾아낸다
    for i in range(len(matrix)):
        for n in range(len(matrix[i])):
            if matrix[i][n] == max:
                lst.append(i)
                lst.append(n)
                break
    # 리스트의 앞 두 자리가 제일 작은 좌표이므로 앞 두 자리만 반환받는다     
    return lst[0:2]
    
    
    
    #             print(i, n)
    #             max_position.append(i)
    #             max_position.append(n)
    # return max_position
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

matrix3 = [
    [9, 2, 5],
    [4, 9, 6],
    [7, 8, 1]
]
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
#####################################################
