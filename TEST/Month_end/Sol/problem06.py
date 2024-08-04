############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    str_num = []
    for str in str_list:
        count = 0
        for _ in str:
            count += 1
        str_num.append(count)
    sorted_str_num = sorted(str_num)
    longest_num = sorted_str_num[-1]
    location = str_num.index(longest_num)
    return str_list[location]
    
    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"
