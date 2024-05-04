dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

from collections import deque


def is_corner(pre_y, pre_x, y, x, ny, nx):
    if pre_y == -1 or pre_x == -1:
        return False

    if (pre_y == y == ny) or (pre_x == x == nx):
        return False
    else:
        return True


def bfs(cost, board, n):
    que = deque()
    cost[0][0] = [100] * 4
    que.append((-1, -1, 0, 0, 0))
    while que:
        pre_y, pre_x, y, x, now_cost = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                pass
            else:
                continue

            if pre_y == ny and pre_x == nx:
                continue

            if board[ny][nx] == 1:
                continue

            sum_cost = now_cost
            if is_corner(pre_y, pre_x, y, x, ny, nx):
                sum_cost += 600
            else:
                sum_cost += 100

            if sum_cost >= cost[ny][nx][i]:
                continue

            cost[ny][nx][i] = sum_cost
            que.append((y, x, ny, nx, sum_cost))

    return min(cost[-1][-1])


def solution(board):
    n = len(board)
    cost = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    return bfs(cost, board, n)


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

