def solution(rows, columns, queries):
    nm = [[0] * (columns + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            nm[i][j] = (i - 1) * columns + j

    rs = []

    for y1, x1, y2, x2 in queries:
        nx = x1
        ny = y1

        temp = nm[ny][nx]

        minv = temp

        for nx in range(x1 + 1, x2 + 1):
            nm[ny][nx], temp = temp, nm[ny][nx]
            minv = min(nm[ny][nx], minv)

        for ny in range(y1 + 1, y2 + 1):
            nm[ny][nx], temp = temp, nm[ny][nx]
            minv = min(nm[ny][nx], minv)

        for nx in range(x2 - 1, x1 - 1, -1):
            nm[ny][nx], temp = temp, nm[ny][nx]
            minv = min(nm[ny][nx], minv)

        for ny in range(y2 - 1, y1 - 1, -1):
            nm[ny][nx], temp = temp, nm[ny][nx]
            minv = min(nm[ny][nx], minv)

        rs.append(minv)

    return rs

