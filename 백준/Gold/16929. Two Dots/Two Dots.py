import sys

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def bfs(py, px, y, x, visited, color):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (
            0 <= ny < len(maps)
            and 0 <= nx < len(maps[0])
            and maps[ny][nx] == color
            and not (ny == py and nx == px)
        ):
            if (ny, nx) in visited:
                return True

            visited.add((ny, nx))
            if bfs(y, x, ny, nx, visited, color):
                return True


def main():
    visited = set()
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if bfs(None, None, r, c, visited, maps[r][c]):
                print("Yes")
                return

    print("No")


main()
