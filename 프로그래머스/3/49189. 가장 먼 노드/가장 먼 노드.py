from collections import deque

def solution(n, edge):
    w = [0] * (n + 1)
    
    dic = {i: [] for i in range(1, n + 1)}
    visited = [False] * (n + 1)
    visited[1] = True
    
    for a, b in edge:
        dic[a].append(b)
        dic[b].append(a)
    
    que = deque([(1, 0)])
    
    max_v = 0
    while que:
        start, k = que.popleft()
        for end in dic[start]:
            if visited[end]:
                continue
                
            visited[end] = True
            w[end] = k + 1
            que.append((end, k + 1))
            max_v = max(max_v, k + 1)
    
    return len([i for i in w if i == max_v])