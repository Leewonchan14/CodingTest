import sys


def dfs(i, computers, visited):
    for j in range(len(computers)):
        if not visited[j] and computers[i][j] == 1:
            visited[j] = True
            dfs(j, computers, visited)


def solution(n, computers):
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i, computers, visited)

    return cnt


