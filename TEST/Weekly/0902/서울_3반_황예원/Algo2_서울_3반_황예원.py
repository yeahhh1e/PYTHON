T = int(input())
for tc in range(1, T+1):
    N = int(input())
    string = str(input())
    print_list = []
    for s in string:  # 받은 문자열을 순회하며 아스키코드로 변환
        asc = ord(s)
        binary_num = bin(asc)   # 이진수로 변환
        b_list = binary_num[2:] # 앞에 0b 떼주기

        # 중위순회 하기
        # 어차피 자릿수는 7자리이므로 중위순회 순서대로 리스트에 넣어주기
        sort_list = b_list[3]+b_list[1]+b_list[4]+b_list[0]+b_list[5]+b_list[2]+b_list[6]
        print_list.append(sort_list)
    print(f"#{tc}", *print_list)
