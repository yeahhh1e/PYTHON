matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.
matrix_len = 0
print(len(matrix))
for i in matrix:
    print(f'{i} 리스트는 {len(i)}개 만큼 요소를 가지고 있습니다.')

# for number in matrix:
#     temporary_len = 0
#     i = 0

#     for i in number:
#         print(number)
#         print(f'번째 요소의 값은{i}입니다.')
#         temporary_len += 1

# for 
temporary_len = 0
for index, number in enumerate(matrix):
    for index_2, i in enumerate(number):
        temporary_len += 1
        i = 0
        print(f'matrix의 {index},{index_2} 번째 요소의 값은 {matrix[index][index_2]} 입니다.')

