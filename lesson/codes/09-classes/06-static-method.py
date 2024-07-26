class StringUtils:
    def __init__(self):
        pass # pass를 쓰더라도 쓰는 것을 권장

    # 클래스가 호출하는 method들 -> 인스턴스를 만들지 않아도 됨
    @staticmethod
    def reverse_string(string):
        return string[::-1]
    
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()

text = 'hello, world'

# result1 = StringUtils.reverse_string(text)
# print(result1)

instance1 = StringUtils()
print(instance1.reverse_string(text)) # dlrow ,olleh 기능상으로 접근을 막은 것은 아님