############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    pass
    # # 여기에 코드를 작성하여 함수를 완성합니다.
    def count_string(str):
        cnt = 0
        for _ in str:
            cnt += 1
        return cnt

    length_lst = list(map(count_string, str_list))
    max_length = length_lst[0]
    for n in length_lst:
        if max_length < n:
            max_length = n

    max_index = 0
    for i in length_lst:
        if max_index < i:
            max_index = i

    count = 0
    for length in length_lst:
        if length == max_index:
            break
        else:
            count +=1
    print(length_lst[count])

            
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"
