from collections import deque


def isGoodPoint(y, x, places):
    return 0 <= y < len(places) and 0 <= x < len(places[0]) and places[y][x] != "X"


dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def isGap2In(places, start, end):
    y, x = start
    que = deque()
    visited = set()
    que.append((y, x, 0))
    visited.add((y, x))

    while que:
        y, x, cnt = que.popleft()

        if end[0] == y and end[1] == x and cnt <= 2:
            return True

        if cnt > 2:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not isGoodPoint(y, x, places):
                continue

            visited.add((ny, nx))
            que.append((ny, nx, cnt + 1))

    return False


def points(places):
    result = []

    for r in range(len(places)):
        for c in range(len(places[r])):
            if places[r][c] == "P":
                result.append((r, c))

    return result


def allGood(places):
    pts = points(places)

    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            if isGap2In(places, pts[i], pts[j]):
                return False

    return True


def solution(places):
    return [1 if allGood(p) else 0 for p in places]
