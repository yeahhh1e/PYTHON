############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 min, max, sorted 함수 리스트 메서드 sort 를 사용하지 않습니다.
def population_difference(population_list):
    # pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 최대 인구 수를 구한다
    max_population = 0
    for i in population_list:
        if i > max_population: # max_population에는 list를 순회하며 제일 큰 값이 i에 들어가게 된다
            max_population = i

    min_population = population_list[0] # 우선 기본값을 인덱스 0번으로 설정해준다
    for i in population_list:
        if i < min_population: # 리스트를 순회하며 제일 작은 값이 i에 들어가게 된다
            min_population = i
    
    return max_population - min_population # 둘의 차이를 구한다



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(population_difference([100, 200, 300, 400, 500]))  # 400
print(population_difference([50, 150, 250]))  # 200
print(population_difference([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))  # 90
####################################################
