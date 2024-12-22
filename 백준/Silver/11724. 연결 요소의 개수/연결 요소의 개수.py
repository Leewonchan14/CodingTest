import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def main(dic, n):
    visited = [False] * (n + 1)

    def dfs(start):
        for nn in dic[start]:
            if not visited[nn]:
                visited[nn] = True
                dfs(nn)

    cnt = 0
    for i in dic.keys():
        if not visited[i]:
            cnt += 1
            visited[i] = True
            dfs(i)

    return cnt


n, m = map(int, input().split())

dic = {i + 1: [] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

print(main(dic, n))
