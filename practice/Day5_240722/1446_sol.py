# 아래 함수를 수정하시오.
# 방법 1
print("방법 1")
def find_min_max(lst):
    x = min(lst)
    y = max(lst)
    min_max = (x,) + (y,)
    return min_max

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)

# 방법 2
print("방법 2")
def find_min_max_2(lst):
    lst.sort()
    x = lst[0]
    y = lst[-1]
    min_max = (x,) + (y,)
    return min_max

result = find_min_max_2([3, 1, 7, 2, 5])
print(result)  # (1, 7)

