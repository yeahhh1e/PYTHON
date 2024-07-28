books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

# books[0], books[3] = books[3], books[0]
# authors[0], authors[1], authors[2], authors[3] = authors[1], authors[3], authors[0], authors[2]
# print(authors)
# new_dict = dict(zip(authors, books))
# print(new_dict)

print(f'{authors[1]} : {books[3]}\n{authors[3]} : {books[1]}\n{authors[0]} : {books[2]}\n{authors[2]} : {books[0]}\n{authors[-1]} : {books[-1]}')