from collections import deque
import heapq

def solution(N, road, K):
    weights = [float('inf')] * (N + 1)
    weights[1] = 0
    
    dic = {}
    for a,b,c in road:
        dic[a] = dic.get(a, [])
        dic[b] = dic.get(b, [])
        dic[a].append((b, c))
        dic[b].append((a, c))
    
    que = deque([1])
    
    while que:
        start = que.popleft()
        
        for end, w in dic[start]:
            if weights[start] + w < weights[end]:
                weights[end] = weights[start] + w
                que.append(end)
                
    return len(list(filter(lambda x: x <= K, weights)))
            
    
    