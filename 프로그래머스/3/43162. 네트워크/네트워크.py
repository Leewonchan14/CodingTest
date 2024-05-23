from collections import deque

def solution(n, computers):
    dic = {i:[] for i in range(n)}
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 0:
                continue
            dic[i].append(j)
            dic[j].append(i)
    
    count = 0
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        
        count += 1
        visited[i] = True
        que = deque([i])
        while que:
            e = que.popleft() 
            for ne in dic[e]:
                if visited[ne]:
                    continue
                visited[ne] = True
                que.append(ne)
                
    return count
            