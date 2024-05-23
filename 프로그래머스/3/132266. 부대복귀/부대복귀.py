from collections import deque

def solution(n, roads, sources, destination):
    dic = {i: [] for i in range(n + 1)}
    for a, b in roads:
        dic[a].append(b)
        dic[b].append(a)
        
    dp = [-1] * (n + 1)
    dp[destination] = 0
    que = deque([(destination, 0)])
    
    while que:
        s,cnt = que.popleft()
        
        for e in dic[s]:
            if dp[e] != -1:
                continue
                
            dp[e] = cnt + 1
            que.append((e, cnt + 1))
            
    return [dp[s] for s in sources]
                
    