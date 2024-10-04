from collections import deque


def bfs(visited, weights, start, destination):
    pass

def solution(n, roads, sources, destination):
    weights = [-1] * (n + 1)
    visited = [False] * (n + 1)
    dic = {}
    for a, b in roads:
        dic[a] = dic.get(a, [])
        dic[b] = dic.get(b, [])
        dic[a].append(b)
        dic[b].append(a)
    
    visited[destination] = True
    weights[destination] = 0
    que = deque([(destination, 0)])
    
    while que:
        start, k = que.popleft()
        
        for end in dic.get(start,[]):
            if visited[end]:
                continue
            visited[end] = True
            que.append((end, k + 1))
            weights[end] = k + 1
            
    
    return list(map(lambda x: weights[x], sources))
            
    
    