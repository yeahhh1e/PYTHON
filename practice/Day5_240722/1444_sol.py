# 아래 함수를 수정하시오.
def even_elements(lst):
    even_lst = []
    while lst:
        i = lst.pop()
        if i % 2 == 0:
            even_lst.extend([i])
    even_lst.reverse()
    result = even_lst
    return result
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
