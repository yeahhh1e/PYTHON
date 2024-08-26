# 보물의 가격 표
treasure_prices = {
    "gold": 100,
    "silver": 50,
    "diamond": 200,
    "ruby": 150,
    "emerald": 120,
    "sapphire": 180,
    "pearl": 80,
    "coin": 1
}

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_total_value(treasure_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    # 리스트를 순회하며 prices의 키랑 같은게 있는지 확인
    # 같다면 prices의 해당 키의 값을 가져와 sum에 넣음
    # sum을 반환함
    sum = 0
    lst = treasure_prices.keys()
    for t in treasure_list:
        for i in lst:
            if i == t:
                sum += treasure_prices[i]
    return sum

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_total_value(["gold", "silver", "diamond", "gold", "silver"]))  # 500
print(calculate_total_value(["pearl"]))  # 80
#####################################################
