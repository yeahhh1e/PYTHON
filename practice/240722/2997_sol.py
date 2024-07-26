
original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr.extend(original_word)
print(arr)
#['코', '딩', ' ', '공', '부', '는', 'ㄴ', ' ', '1', '일', 'ㄹ', ' ', '1', '커', 'ㅓ',
#  '밋', 'ㅅ', ' ', '@', '@', '@', '#', '^', '(', ')', '#', '_', '+', '!', '&', '~', 
# ':', '"']

def restructure_word(word, arr):
    i = 0
    # word에서 순회중인 문자열이 숫자이면 그 숫자만큼 pop 함수를 반복하여 arr에서 마지막 요소를 제거한다.
    while i < len(word):
        if word[i].isdecimal():
            count = int(word[i])
            for n in range(count):
                arr.pop()
    # 이외의 경우라면 arr에서 해당 문자열을 제거한다.
        else:
            arr.remove(word[i])
        i += 1
    return arr

result = restructure_word(word, arr)
print(result)
result2 = ''.join(result)
print(result2)
