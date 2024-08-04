############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    max_num = -999999
    # matrix를 순회하며 초기 설정 값 max 보다 크면 max 값을 해당 값으로 바꾼다
    for i in range(len(matrix)):
        for j in range(len(matrix[0])): # matrix[0] 으로 열의 수로 해줘야 런타임 오류 나지 않음
            # 해당 값 주변과 더한 총 합 total
            total = 0
            # 상하좌우 인덱스 순회
            for x, y in ((i, j), (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)): # 튜플이 아닌 리스트로 해도 동일한 결과
                # 인덱스의 값이 0보다 크고 매트릭스의 크기보다 작아야 오류가 발생하지 않음
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]): 
                    total += matrix[x][y]
                
            if max_num < total:
                max_num = total
    
    return max_num
    
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
