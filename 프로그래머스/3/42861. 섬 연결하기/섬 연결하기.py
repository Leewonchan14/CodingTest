from queue import PriorityQueue
from collections import deque
def mst(n, que):    
    set_ls = [set([i]) for i in range(n)]
    ls = []
    
      # and len(set_ls[0]) != n
    while que.queue :
        weight, a, b = que.get()
        if set_ls[a] == set_ls[b]:
            continue
            
        set_ls[a] = set_ls[a] | set_ls[b]
        
        for s in set_ls[a]:
            set_ls[s] = set_ls[a]
        
        ls.append(weight)
                
    return sum(ls)


def solution(n, costs):
    que = PriorityQueue()
    for a,b,weight in costs:
        que.put((weight, a, b))
        
    coast = mst(n, que)
    return coast

    
    