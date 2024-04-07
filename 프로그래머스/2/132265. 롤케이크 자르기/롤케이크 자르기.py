def solution(topping):
    a_dic = {}
    a_len = 0
    b_dic = {}
    for t in topping:
        b_dic[t] = b_dic.get(t, 0) + 1
        
    b_len = len(b_dic.keys())
    
    index = 0
    ls = []
    while index < len(topping):
        if topping[index] not in a_dic:
            a_len += 1
        a_dic[topping[index]] = a_dic.get(topping[index] , 0) + 1
        
        pop = b_dic.pop(topping[index])
        if pop - 1 == 0:
            b_len -= 1
        else:
            b_dic[topping[index]] = pop - 1
            
        if a_len == b_len:
            ls.append(index)
        
        index += 1
        
    return len(ls)