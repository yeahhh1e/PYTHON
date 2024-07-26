# 아래 함수를 수정하시오.
# 방법 1
print("방법 1")
def remove_duplicates(original_list):
    new_lst = []
    for i in original_list:
        # new_lst에 i가 없으면 추가
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)


# 방법 2
print("방법 2")

def remove_duplicates_2(original_list):
    new_lst2 = []
    i = 0
    # original_list 순회
    while i < len(original_list):
        # 만약 new_lst2에 original_list i번째 요소가 있으면 original_list에서 해당 요소 제거
        if original_list[i] in new_lst2:
            original_list.remove(original_list[i])
        else:
            # 없으면 new_lst2에 추가하고 i값 1 증가
            new_lst2.append(original_list[i])
            i += 1
    return new_lst2

result = remove_duplicates_2([1, 2, 2, 3, 4, 4, 5])
print(result)