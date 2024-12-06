def solution(clothes):
    dic = {}
    for v, k in clothes:
        dic[k] = dic.get(k, 0) + 1
    
    mul =  1
    for i in dic.values():
        mul *= i + 1
    
    return mul - 1