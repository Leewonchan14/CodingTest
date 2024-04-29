from queue import PriorityQueue

def daikstra(N, dic, K):
    que = PriorityQueue();
    
    weights = [float('inf')] * (N + 1)
    weights[1] = 0
    
    que.put((0, 1))
    while que.queue:
        weight, start = que.get()
        
        for n_weight, n in dic.get(start, []):
            if weight + n_weight < weights[n]:
                weights[n] = weight + n_weight
                que.put((weight + n_weight, n))

    
    return len([w for w in weights if w <= K])
    

def solution(N, road, K):
    dic = {}
    for a,b,c in road:
        dic[a] = dic.get(a, [])
        dic[a].append((c, b))
        
        dic[b] = dic.get(b, [])
        dic[b].append((c, a))
        
    return daikstra(N, dic, K)
