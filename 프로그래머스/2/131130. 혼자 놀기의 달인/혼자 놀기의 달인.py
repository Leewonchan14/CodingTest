def solution(cards):
    is_open = [False] * (len(cards) + 1)
    ls = [0]
    for i in cards:
        ls.append(i)
        
    cards = ls
    
    ls = []
    
    count = 0
    
    for i in range(1, len(cards)):
        if not is_open[i]:
            index = i
            while not is_open[index]:
                is_open[index] = True
                count += 1
                index = cards[index]
            ls.append(count)
            count = 0
            
            
    if len(ls) <= 1:
        return 0
    
    ls.sort()
    return ls[-1] * ls[-2]