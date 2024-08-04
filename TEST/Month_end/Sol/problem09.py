############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_number_sum(word):
    pass
    # # 여기에 코드를 작성하여 함수를 완성합니다.
    n_hap = 0 # 숫자를 합할 변수
    n_tem = "" # 숫자 저장할 변수

    for i in word:
        if i.isdigit() == True: 
            n_tem += i # 숫자면 n_tem에 저장
        elif n_tem : # 숫자가 아니면
            n_hap += int(n_tem) # n_hap에 여태 저장한 숫자를 저장
            n_tem = "" # n_tem 초기화
    
    if n_tem:
        return n_hap + int(n_tem)
    else:
        return n_hap


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_number_sum('ab123cd45ef6'))     # 174
print(calculate_number_sum('0a1s2d3f4'))        # 10
print(calculate_number_sum('ssafy10gi2good4560')) # 4572
#####################################################
