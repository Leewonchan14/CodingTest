def solution(cards):
    isOpen =  [False for i in range(len(cards))]
    open_box_count_list = []
    count = 0
    index = 0
    while True:
        # 이미 열려 있다면
        if isOpen[index]:
            # 지금까지 연 상자의 갯수를 append 하고 다음 index를 찾는다.
            open_box_count_list.append(count)
            count = 0
            # isOpen에서 false가 나오면 된다.
            for i in range(len(isOpen)):
                if isOpen[i] == False:
                    index = i
                    break
                    
            # 만약 다 열려있다면 while문을 나온다.
            if i == len(isOpen) - 1 and isOpen[i] != False:
                break
            
        # 상자를 연다
        isOpen[index] = True
        count += 1
        
        # 다음 index를 확인한다.    
        index = cards[index] - 1;
        
    open_box_count_list.sort()
    return open_box_count_list[-1] * open_box_count_list[-2] if len(open_box_count_list) >= 2 else 0