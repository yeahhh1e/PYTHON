data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
# for i in data:
#     if i['name']
# data.get[i]
for i in data:
    # data에서 순회하면서 key_list에 있는 키얻기
    key_name = i.get('name', Unkn)
        
    # print 
    # # 가 없다면 key : unknown 할당
    # if k not in item:
    #     data.setdefault(k, 'unknown')
    # print(f'{k} 은/는 {data.get(k)}입니다.')