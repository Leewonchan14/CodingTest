import sys

input = sys.stdin.readline
n = int(input())
dic = {i: set() for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

arr = [int(i) for i in input().split()]

visited = [False] * (n + 1)
cnt = 0
ret = True


def dfs(x):
    global cnt, ret

    if cnt >= len(arr):
        return True

    not_visited = set([i for i in dic[x] if not visited[i]])

    for _ in range(len(not_visited)):
        nx = arr[cnt]

        if nx not in not_visited:
            ret = False
            return True

        cnt += 1
        visited[nx] = True
        dfs(nx)


def main():
    if arr[0] != 1:
        return 0

    global cnt, ret
    visited[arr[0]] = True
    cnt += 1
    dfs(arr[0])

    if ret == False or any([not visited[i] for i in range(1, n + 1)]):
        return 0
    return 1


print(main())
