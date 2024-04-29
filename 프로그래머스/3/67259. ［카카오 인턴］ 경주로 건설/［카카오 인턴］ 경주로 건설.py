from collections import deque
from queue import PriorityQueue

ls = [0, 0]


def is_corner(pre, start, end):
    pre_y, pre_x = pre
    start_y, start_x = start
    end_y, end_x = end

    if start_y == 0 and start_x == 0:
        return False

    return not (start_y - pre_y == end_y - start_y and start_x - pre_x == end_x - start_x)


def bfs(board):
    length = len(board)
    visited = [[[float('inf')] * 4 for _ in range(length)] for _ in range(length)]
    que = PriorityQueue()
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    que.put((0, 0, 0, 0, 0))
    for i in range(4):
        visited[0][0][i] = 0

    while not que.empty():
        bill, y, x, pre_y, pre_x = que.get()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < length and 0 <= nx < length:
                if board[ny][nx] == 1:
                    continue

                n_bill = bill + 100
                if is_corner((pre_y, pre_x), (y, x), (ny, nx)):
                    n_bill += 500

                if n_bill > visited[ny][nx][i]:
                    continue

                visited[ny][nx][i] = n_bill
                que.put((n_bill, ny, nx, y, x))

    return min(visited[length - 1][length - 1])


def solution(board):
    return bfs(board)


# print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
#                 [0, 0, 0, 0, 0, 0]]))
