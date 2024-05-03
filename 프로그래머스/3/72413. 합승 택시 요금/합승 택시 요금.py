from collections import deque


def solution(n, s, a, b, fares):
    dic = {i: {} for i in range(1, n + 1)}
    for start, end, coast in fares:
        dic[start][end] = coast
        dic[end][start] = coast

    result = {}

    for i in range(1, n + 1):
        result[i] = bfs(i, dic)

    result = sorted(result.items(), key=lambda x: x[1][s] + x[1][a] + x[1][b])

    smallest = result[0][1]

    return smallest[a] + smallest[b] + smallest[s]


def bfs(start, dic):
    result = {i + 1: float('inf') for i in range(len(dic))}

    result[start] = 0

    que = deque()
    que.append((start, 0))
    while que:
        idx, now_coast = que.popleft()

        for next_node, coast in dic[idx].items():
            if now_coast + coast < result[next_node]:
                result[next_node] = now_coast + coast
                que.append((next_node, result[next_node]))

    return result


