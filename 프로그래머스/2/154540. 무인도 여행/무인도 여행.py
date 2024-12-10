import sys

sys.setrecursionlimit(10 ** 9)

def isCorrectPoint(y, x, maps, visited):
    return 0 <= y < len(maps) and 0 <= x < len(maps[y]) and maps[y][x] != "X" and not visited[y][x] 

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x, maps, visited):
    sum = int(maps[y][x])
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if isCorrectPoint(ny, nx, maps, visited):
            visited[ny][nx] = True
            sum += dfs(ny, nx, maps, visited)
    
    return sum

def solution(maps):
    result = []
    visited = [[False] * len(r) for r in maps]
    for r in range(len(maps)):
        for c in range(len(maps[r])):
            if isCorrectPoint(r, c, maps, visited):
                visited[r][c] = True
                result.append(dfs(r, c, maps, visited))
                
    result.sort()
    
    return result if result else [-1]