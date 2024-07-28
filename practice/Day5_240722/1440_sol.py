# 아래 함수를 수정하시오.
# 방법 1
print('방법 1')
def reverse_string(word):
    word = list(word)
    word.reverse()
    str = ''.join(word)
    return str

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

# 방법 2
print('방법 2')
reverse = "Hello, World!"
reverse_string_2 = ''
for i in reverse:
    reverse_string_2 = i + reverse_string_2 # i를 앞에다가 붙임

print(reverse_string_2)