def dfs(visited, start, computers):
    for end in range(len(computers)):
        if visited[end] or computers[start][end] != 1:
            continue
        visited[end] = True
        dfs(visited, end, computers)
        
        
    

def solution(n, computers):
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(visited, i, computers)
            
    return cnt