from collections import deque


class Length:
    maps = []
    visited = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def __init__(self, maps):
        self.maps = maps
        self.visited = [[False] * len(c) for c in maps]

    def isInnerPoint(self, y, x):
        return (
            0 <= y < len(self.maps)
            and 0 <= x < len(self.maps[0])
            and not self.visited[y][x]
            and self.maps[y][x] == 1
        )

    def isTarget(self, y, x):
        return y == len(self.maps) - 1 and x == len(self.maps[0]) - 1

    def bfs(self):
        que = deque([])
        que.append((0, 0, 1))
        while que:
            y, x, cnt = que.popleft()
            if self.isTarget(y, x):
                return cnt

            for i in range(4):
                ny = y + self.dy[i]
                nx = x + self.dx[i]
                if self.isInnerPoint(ny, nx):
                    self.visited[ny][nx] = True
                    que.append((ny, nx, cnt + 1))

        return -1


def solution(maps):
    return Length(maps).bfs()
