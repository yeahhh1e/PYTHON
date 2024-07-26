# MMS LMS 의 공통 class 는

class SMS:
    # class variable
    provider = 'SKT'

    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message
        # print('SMS class is created')

    def send(self):
        print(f'SMS sent to {self.phone_number} (provider: {self.provider})')

    # class method example
    @classmethod
    def send_bulk_sms(cls, phone_numbers, message):
        for phone_number in phone_numbers:
            cls(phone_number, message).send()

    # static method example
    @staticmethod
    def is_valid_phone_number(phone_number):
        return len(phone_number) == 13

    # def __str__(self):
    #     return f'{self.phone_number}: {self.message}'

    def __repr__(self):
        return f'SMS({self.phone_number}, {self.message})'


love_sms = SMS('010-1234-5678', 'I love you')
love_sms.send()
SMS.send_bulk_sms(['010-1234-5678', '010-5678-1234'], 'I love you')
print(SMS.is_valid_phone_number('010-1234-5678'))
print(SMS.provider)
print(love_sms.provider)
love_sms.provider = 'KT'
print(love_sms.provider)
print(SMS.provider)
# __str__ method 와 __repr__ method 는 print() 함수를 사용할 때 호출된다.
# __str__ method 는 사용자가 보기 쉽게 출력할 때 사용한다.
# __repr__ method 는 개발자가 객체를 디버깅할 때 사용한다.
#
print(love_sms)
# print(repr(love_sms))

# class LMS(SMS):
#     def __init__(self, phone_number, message, user_id):
#         super().__init__(phone_number, message)
#         self.user_id = user_id
#
#     def send(self):
#         print(f'LMS sent to {self.phone_number} by user_id {self.user_id}')
#
#     @classmethod
#     def send_bulk_sms(cls, phone_numbers, message):
#         for phone_number in phone_numbers:
#             cls(phone_number, message, 'user_id_1234').send()
#
# lms = LMS('010-1234-5678', 'I love you', 'user_id_1234')
# lms.send()
# LMS.send_bulk_sms(['010-1234-5678', '010-5678-1234'], 'I love you')