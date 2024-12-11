from collections import deque

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def goWhile(point, board, i):
    y, x = point
    while True:
        ny = y + dy[i]
        nx = x + dx[i]

        if not (
            0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] != "D"
        ):
            break

        y = ny
        x = nx

    return y, x


def bfs(board, start, end, visited):
    sy, sx = start
    ey, ex = end

    que = deque([])
    que.append((sy, sx, 0))
    visited.add((sy, sx))

    while que:
        y, x, cnt = que.popleft()
        if end[0] == y and end[1] == x:
            return cnt

        for i in range(4):
            ny, nx = goWhile((y, x), board, i)
            if (ny, nx) in visited:
                continue

            visited.add((ny, nx))
            que.append((ny, nx, cnt + 1))

    return -1


def toMap(board):
    return [list(b) for b in board]


def getPoint(board):
    start = None
    end = None

    for r, r_ in enumerate(board):
        for c, c_ in enumerate(r_):
            if c_ == "R":
                start = (r, c)

            if c_ == "G":
                end = (r, c)

    return start, end


def solution(board):
    board = toMap(board)
    start, end = getPoint(board)
    visited = set()
    return bfs(board, start, end, visited)


# solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])
