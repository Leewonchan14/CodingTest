def dfs(start, visited, computers, n):
    for end in range(n):
        if computers[start][end] == 0 or visited[end]:
            continue
            
        visited[end] = True
        dfs(end, visited, computers, n)
    


def solution(n, computers):
    visited = [False] * n
    cnt = 0
    for start in range(n):
        if visited[start]:
            continue
            
        cnt += 1
        visited[start] = True
        dfs(start, visited, computers, n)
            
    return cnt
