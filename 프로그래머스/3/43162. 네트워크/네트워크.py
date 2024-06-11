def dfs(n, visited, dic):
    for i in dic[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i, visited, dic)
    
    

def solution(n, computers):
    visited = [False] * n
    
    dic = {i:[] for i in range(n)}
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                dic[i].append(j)
                dic[j].append(i)
                
    cnt = 0
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i, visited, dic)
            
    return cnt
            
    