############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_days_to_fill_tank(tank_capacity, fill_amount, evaporation_amount):
    # pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 낮 양 + 증발 양 반복해서 총 양이 되는 날
    total = 0
    count = 0
    while True:
        # 낮에 물 추가
        total += fill_amount
        # 총 양이 채워야 하는 양보다 많아지게 되면 while문 종료
        if tank_capacity <= total:
            # 일수 증가
            count += 1
            break
        # 밤에 물 증발
        total -= evaporation_amount
        # 하루가 지남
        count += 1
        
        # if tank_capacity <= total:
        #     break
        
    return count

    # # 하루에 총 추가되는 양 = 채워지는 양 - 증발 양 
    # day_fill = fill_amount - evaporation_amount
    # # 총 용량 나누기 하루 추가 양의 몫 -> 소요 일수
    # day = tank_capacity // day_fill
    # if day * day_fill < tank_capacity:
    #     day += 1
    # return day
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_days_to_fill_tank(100, 20, 5))  # 7
print(calculate_days_to_fill_tank(1000, 100, 10))  # 11
print(calculate_days_to_fill_tank(100, 10, 1))  # 11
#####################################################
