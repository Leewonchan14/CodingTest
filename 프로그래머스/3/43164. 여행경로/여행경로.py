import numpy as np

const = [0]

result = []

ls = ["ICN"]


def recursive(dic):
    if const[0] == len(ls) - 1:
        result.append(ls[:])
        return
    
    for b in dic[ls[-1]]:
        if b[1]:
            continue
        b[1] = True
        ls.append(b[0])
        recursive(dic)
        ls.pop()
        b[1] = False
    
        
    

def solution(tickets):
    dic = {}
    const[0] = len(tickets)
    for a,b in tickets:
        dic[a] = dic.get(a, [])
        dic[b] = dic.get(b, [])
        dic[a].append([b, False])
        
    recursive(dic)
    result.sort(key=lambda x: "".join(x))
    return result[0] if result else []
