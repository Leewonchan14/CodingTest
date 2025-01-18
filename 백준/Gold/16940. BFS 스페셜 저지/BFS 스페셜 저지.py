import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dic = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    dic.setdefault(a, []).append(b)
    dic.setdefault(b, []).append(a)

arr = [int(i) for i in input().split()]

arr_idx = {v: i for i, v in enumerate(arr)}

for i in range(1, n + 1):
    dic[i].sort(key=lambda x: arr_idx[x])


n_arr = []


def bfs(start):
    que = deque()
    visited = [False] * (n + 1)
    que.append(start)
    visited[start] = True
    n_arr.append(start)

    while que:
        x = que.popleft()
        for nx in dic[x]:
            if not visited[nx]:
                que.append(nx)
                n_arr.append(nx)
                visited[nx] = True


def is_same_arr(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True


def main():
    bfs(arr[0])
    if arr[0] != 1:
        return 0
    return 1 if is_same_arr(arr, n_arr) else 0


print(main())
