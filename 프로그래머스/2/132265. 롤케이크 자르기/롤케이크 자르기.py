def solution(topping):
    length = len(topping)
    
    left_dic = {}
    right_dic = {}
    
    answer = 0
    
    for i in range(length):
        topping_item = topping[i]
        
        right_dic[topping_item] = right_dic.get(topping_item, 0) + 1
        
    for i in range(length):
        
        topping_item = topping[i]
        
        left_dic[topping_item] = left_dic.get(topping_item, 0) + 1
        
        
        right_item = right_dic.get(topping_item)
        
        if right_item - 1 == 0:
            right_dic.pop(topping_item)
        else :
            right_dic[topping_item] = right_item - 1
        
        if len(left_dic.keys()) == len(right_dic.keys()):
            answer += 1
            
    return answer
