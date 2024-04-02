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
        

def solution(n, computers):
    dic = {}
    for a in range(len(computers)):
        for b in range(len(computers[0])):
            if a == b or computers[a][b] == 0:
                continue
            dic[a] = dic.get(a, [])
            dic[a].append(b)
            dic[b] = dic.get(b, [])
            dic[b].append(a)
    print(dic)
        
    
    visited = [False] * n
    
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, dic)
            count += 1
            
    return count