def solution(weights):
    
    dic = {}
    
    for weight in weights:
        dic[weight] = dic.get(weight, 0) + 1
        
    count = 0
    keys = dic.keys()
    for key in keys:
        if key % 2 == 0 :
            count += dic[key] * dic.get(key/2 * 3, 0)
            count += dic[key] * dic.get(key/2 * 1, 0)
        if key % 3 == 0 :
            count += dic[key] * dic.get(key/3 * 4, 0)
            count += dic[key] * dic.get(key/3 * 2 ,0) 
        if key % 4 == 0 :
            count += dic[key] * dic.get(key/4 * 3, 0)
        
        count += dic[key] * dic.get(key * 2, 0)
        count += dic[key] *( dic[key] - 1)
        
        
    return count / 2
    
    