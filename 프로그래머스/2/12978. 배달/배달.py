from collections import deque
def solution(N, road, K):
    dic = {i: [] for i in range(0, N + 1)}
    weights = [float('inf') for i in range(0, N + 1)]
    weights[1] = 0
    for a,b,c in road:
        dic[a].append((b, c))
        dic[b].append((a, c))
        
    que = deque([1])
    
    while que:
        s = que.popleft()
        
        for e,w in dic[s]:
            if weights[s] + w >= weights[e]:
                continue
                
            weights[e] = weights[s] + w
            que.append((e))
            
    return len([w for w in weights if w <= K])
    