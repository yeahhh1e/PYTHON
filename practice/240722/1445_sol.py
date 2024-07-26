# 아래 함수를 수정하시오.
# 방법 1
print("방법 1")
def count_character(x, y):
    return x.count(y)

result = count_character("Hello, World!", "o")
print(result)  # 2

# 방법 2
print("방법 2")
def count_character_2(str, i):
    m = 0
    lst = list(str)
    for n in lst:
        if n == i:
            m += 1
    return m
result = count_character_2("Hello, World!", "o")
print(result)  # 2