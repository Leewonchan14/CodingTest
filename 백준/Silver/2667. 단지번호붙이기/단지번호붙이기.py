import sys

input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def main(arr):
    result = []
    visited = [[False] * len(arr[0]) for _ in range(len(arr))]

    def dfs(y, x, cnt=1):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (
                0 <= ny < len(arr)
                and 0 <= nx < len(arr[ny])
                and not visited[ny][nx]
                and arr[ny][nx] == 1
            ):
                visited[ny][nx] = True
                cnt = dfs(ny, nx, cnt + 1)

        return cnt

    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if visited[r][c] or arr[r][c] == 0:
                continue
            
            visited[r][c] = True
            result.append(dfs(r, c))

    print(len(result))
    result.sort()
    for i in result:
        print(i)


n = int(input())
arr = [[int(i) for i in input().strip()] for _ in range(n)]
main(arr)
