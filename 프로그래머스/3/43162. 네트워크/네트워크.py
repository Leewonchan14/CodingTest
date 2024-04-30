from collections import deque
def bfs(i, visited, dic):
    visited[i] = True
    que = deque()
    que.append(i)
    while que:
        i = que.popleft()
        for ni in dic.get(i, []):
            if not visited[ni]:
                visited[ni] = True
                que.append(ni)
        

def dfs(dic, point, visited):
    for n in dic[point]:
        if visited[n]:
            continue
        visited[n] = True
        dfs(dic, n, visited)
        
        
def solution(n, computers):
    dic = [[] for _ in range(n)]
    for a in range(len(computers)):
        for b in range(len(computers[0])):
            if computers[a][b] == 0:
                continue
            dic[a].append(b)
            dic[b].append(a)
        
    visited = [False] * n
    
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(dic, i, visited)
            count += 1
            
    return count