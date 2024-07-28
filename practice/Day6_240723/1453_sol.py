# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, x, y):
    new_dict = dictionary.copy()
    new_dict.setdefault(x, y)
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
