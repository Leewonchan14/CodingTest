from collections import deque


def spinning_90(board):
    result = [[0] * len(board) for _ in range(len(board[0]))]
    for r in range(len(board[0])):
        for c in range(len(board)):
            result[r][c] = board[c][len(board[0]) - 1 - r]

    return result


def spinning_180(board):
    return spinning_90(spinning_90(board))


def spinning_270(board):
    return spinning_180(spinning_90(board))


def is_equals(cnt_a, table_a, cnt_b, table_b):
    if cnt_a < cnt_b:
        return False

    r_a = len(table_a)
    r_b = len(table_b)

    c_a = len(table_a[0])
    c_b = len(table_b[0])

    if r_a != r_b or c_a != c_b:
        return False

    for r in range(r_a):
        for c in range(c_a):
            if table_b[r][c] != table_a[r][c]:
                return False

    return True


def equals(cnt_a, table_a, cnt_b, table_b):
    spinning1 = spinning_90(table_b)
    spinning2 = spinning_90(spinning1)
    spinning3 = spinning_90(spinning2)

    for s in [table_b, spinning1, spinning2, spinning3]:
        if is_equals(cnt_a, table_a, cnt_b, s):
            return True

    return False


def bfs(y, x, visited, game_board, target):
    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]

    puzzle = []

    min_y, min_x, max_y, max_x = y, x, y, x

    que = deque()
    que.append((y, x))
    visited[y][x] = True
    cnt = 0
    while que:
        y, x = que.popleft()
        cnt += 1
        puzzle.append((y, x))
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        max_x = max(max_x, x)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < len(visited) and 0 <= nx < len(visited[0])):
                continue

            if visited[ny][nx] or game_board[ny][nx] != target:
                continue

            visited[ny][nx] = True
            que.append((ny, nx))
    result = [[0] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for y, x in puzzle:
        result[y - min_y][x - min_x] = 1

    return cnt, result


def solution(game_board, table):
    # game_board = [[1, 1, 0], [0, 1, 1]]
    visited_a = [[False] * len(game_board[0]) for _ in range(len(game_board))]
    visited_b = [[False] * len(game_board[0]) for _ in range(len(game_board))]
    blank = []
    puzzle = []
    for r in range(len(game_board)):
        for c in range(len(game_board[0])):
            if not visited_a[r][c] and game_board[r][c] == 0:
                blank.append(bfs(r, c, visited_a, game_board, 0))

            if not visited_b[r][c] and table[r][c] == 1:
                puzzle.append(bfs(r, c, visited_b, table, 1))

    visited_b = set()
    visited_p = set()
    cnt = 0
    for i in range(len(blank)):
        for j in range(len(puzzle)):
            b = blank[i]
            p = puzzle[j]
            if i not in visited_b and j not in visited_p and equals(*b, *p):
                visited_b.add(i)
                visited_p.add(j)
                cnt += b[0]

    return cnt


