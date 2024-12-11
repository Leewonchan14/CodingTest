mapper = {"X": "O", "O": "X"}


def isWin(visited, now):
    os = [(k, v) for k, v in visited.items() if v == now]
    dic = {}
    for k, v in os:
        r, c = k
        dic[(r + c, "+")] = dic.get((r + c, "+"), 0) + 1
        dic[(r - c, "-")] = dic.get((r - c, "-"), 0) + 1
        dic[(r, "r")] = dic.get((r, "r"), 0) + 1
        dic[(c, "c")] = dic.get((c, "c"), 0) + 1

    if dic.values() and max(dic.values()) >= 3:
        return True

    return False


def isOver(visited):
    o = isWin(visited, "O")
    x = isWin(visited, "X")
    return o or x


def count(board):
    oc = 0
    xc = 0
    for r in board:
        for c in r:
            if c == "O":
                oc += 1
            elif c == "X":
                xc += 1

    if xc > oc or oc - xc > 1:
        return False
    return True


def recursion(board, now, visited):
    rt = None
    rest = []
    isOverFlag = isOver(visited)
    for r in range(3):
        for c in range(3):
            if (r, c) in visited:
                continue

            if isOverFlag and (board[r][c] == mapper[now] or board[r][c] == now):
                return

            if board[r][c] == mapper[now]:
                rest.append((r, c))

            if board[r][c] != now:
                continue

            visited[(r, c)] = now
            rt = recursion(board, mapper[now], visited)
            if rt == 1:
                return 1
            visited.pop((r, c))

    if not rest:
        return 1


def solution(board):
    if not count(board):
        return 0
    key = recursion(
        board,
        "O",
        {},
    )
    return key if key == 1 else 0


# print(solution(["...", ".X.", "..."]))
