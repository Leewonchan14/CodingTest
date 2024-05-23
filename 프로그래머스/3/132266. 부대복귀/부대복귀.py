from collections import deque

def solution(n, roads, sources, destination):
    dic = {i: [] for i in range(n + 1)}
    for a, b in roads:
        dic[a].append(b)
        dic[b].append(a)
        
    visited = [False] * ( n + 1 )
    dp = [-1] * (n + 1)
    que = deque()
    visited[destination] = True
    dp[destination] = 0
    que.append((destination, 0))
    
    while que:
        s,cnt = que.popleft()
        dp[s] = cnt
        
        for e in dic[s]:
            if visited[e]:
                continue
                
            visited[e] = True
            que.append((e, cnt + 1))
            
    return list(map(lambda x: dp[x], sources))
                
    