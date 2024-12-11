dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def lotate(y1, x1, y2, x2, maps):
    minv = float("inf")

    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    y, x = y1, x1
    temp = maps[y][x]
    for i in range(4):
        while True:
            minv = min(minv, maps[y][x])
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < y1 or ny > y2 or nx < x1 or nx > x2:
                break

            temp, maps[ny][nx] = maps[ny][nx], temp
            y = ny
            x = nx

    return minv


def makeMap(rows, columns):
    return [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]


def solution(rows, columns, queries):
    maps = makeMap(rows, columns)
    result = []
    for query in queries:
        result.append(lotate(*query, maps))

    return result
