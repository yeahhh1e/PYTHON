zero_list = [0]
print(zero_list)

# 풀이 1
many_zero_list_str = list('0' * 250000)
many_zero_list = list(map(int, many_zero_list_str))
# print(many_zero_list)
print(len(many_zero_list))

# 아래를 참고
# test_list = ['1', '4', '3', '6', '7']

# # # using map() to
# # # perform conversion
# test_list = list(map(int, test_list))

# # Printing modified list
# print("Modified list is : " + str(test_list))


# 풀이 2 (이게 더 간단하다 !)

many_zero_list = zero_list*250000
print(many_zero_list)


numbers = list(range(1,11))
print(numbers)
print(numbers[3:])