import itertools

def mul(ls):
    rt = 1
    for i in ls:
        rt *= i
    return rt

sumv = [0]
ls = []

def track(num, N, visited, dic):
    if num == N:
        sumv[0] += mul(ls)
        print(ls)
        return 
    
    for k in dic.keys():
        if not visited[k]:
            visited[k] = True
            ls.append(dic[k])
            track(num + 1, N, visited, dic)
            visited[k] = False
            ls.pop()
        

def solution(clothes):
    dic = {}
    for name, type in clothes:
        dic[type] = dic.get(type, 0) + 1
        
    return mul([i + 1 for i in dic.values()]) - 1
