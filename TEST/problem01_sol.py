lst = [49, 39 , 60 , 76, 65]
def min_score(list):
    list.sort()
    return list[0]

print(min_score(lst))