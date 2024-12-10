def isEqual(a, b):
    return (a[0] == b[0] and a[1] == b[1]) or (a[0] == b[1] and a[1] == b[0])


def dfs(tree, n, start, visited, nothing):
    cnt = 1
    visited[start] = True
    for i in tree[start]:
        if visited[i] or isEqual([start, i], nothing):
            continue

        visited[i] = True
        cnt += dfs(tree, n, i, visited, nothing)

    return cnt


def solution(n, wires):
    tree = {i: [] for i in range(n + 1)}
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    c = float("inf")
    for nothing in wires:
        visited = [False] * (n + 1)
        a = dfs(tree, n, nothing[0], visited, nothing)
        b = dfs(tree, n, nothing[1], visited, nothing)

        c = min(abs(a - b), c)

    return c


