def solution(lottos, win_nums):
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    
    zero_count = lottos.count(0)
    
    return [7 - (count + zero_count) if count + zero_count != 0 else 6 , (7 - count) if count != 0 else 6 ]
    