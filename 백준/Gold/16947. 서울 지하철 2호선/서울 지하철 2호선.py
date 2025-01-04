import sys

sys.setrecursionlimit(10**9)
from collections import deque

input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
    a, b = map(int, input().split())
    dic[a] = dic.get(a, [])
    dic[a].append(b)
    dic[b] = dic.get(b, [])
    dic[b].append(a)

result = [0] * (n + 1)

cycle = [False] * (n + 1)


def set_cycle():
    visited = [False] * (n + 1)
    li = [1]
    edge = 0

    def dfs(pre, k):
        nonlocal edge
        for nk in dic[k]:
            if pre != nk and not visited[nk]:
                li.append(nk)
                visited[nk] = True
                if dfs(k, nk):
                    return True

                li.pop()

            elif pre != nk and visited[nk]:
                edge = nk
                return True

    visited[1] = True
    dfs(None, 1)
    for i in range(li.index(edge), len(li)):
        cycle[li[i]] = True


def solve():
    three = []
    for i in range(1, n + 1):
        if cycle[i] and len(dic[i]) >= 3:
            three.append(i)

    for t in three:
        que = deque()
        que.append((t, 0))
        visited = set()
        visited.add(t)
        while que:
            k, cnt = que.popleft()
            result[k] = cnt
            for nk in dic[k]:
                if cycle[nk] or nk in visited:
                    continue

                visited.add(nk)
                que.append((nk, cnt + 1))


def main():
    set_cycle()
    solve()
    print(*[result[i] for i in range(1, n + 1)])


main()
