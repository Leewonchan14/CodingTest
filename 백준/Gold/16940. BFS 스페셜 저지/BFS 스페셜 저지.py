import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dic = {i: set() for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

arr = [int(i) for i in input().split()]


def is_same_arr(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True


def bfs(start):
    que = deque()
    cnt = 1
    visited = [False] * (n + 1)
    que.append(start)
    visited[start] = True

    while que:
        x = que.popleft()
        not_visited = [i for i in dic[x] if not visited[i]]
        n_arr = arr[cnt : cnt + len(not_visited)]
        if n_arr and not all([i in dic[x] for i in n_arr]):
            return 0

        for nx in n_arr:
            visited[nx] = True
            cnt += 1
            que.append(nx)

    if all([visited[i] for i in range(1, n + 1)]):
        return 1

    return 0


def main():
    if arr[0] != 1:
        return 0
    return bfs(arr[0])


print(main())
