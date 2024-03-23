import sys

sys.setrecursionlimit(1000000)


def dfs(row, col, isGo, land, now_count, l):
    # 땅보다 큰곳에 왔다면 return
    if col < 0 or col >= len(land[0]) \
            or row < 0 or row >= len(land):
        return now_count

    # 이미 간 곳이라면 return
    if isGo[row][col]:
        return now_count

    # 빈 땅이라면
    if land[row][col] == 0:
        return now_count

    land[row][col] = l
    # 먼저 석유 갯수 증가와 isGo 표시
    now_count += 1
    isGo[row][col] = True

    # 오른쪽
    now_count = dfs(row, col + 1, isGo, land, now_count, l)
    # 왼쪽
    now_count = dfs(row, col - 1, isGo, land, now_count, l)
    # 아래
    now_count = dfs(row + 1, col, isGo, land, now_count, l)
    # 위
    now_count = dfs(row - 1, col, isGo, land, now_count, l)

    return now_count


def solution(land):
    isGo = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    oils = {0: 0}
    result = 0
    for row in range(len(land)):
        for col in range(len(land[0])):
            count = dfs(row, col, isGo, land, 0, len(oils) + 1)
            if count != 0:
                oils[len(oils) + 1] = count

    for col in range(len(land[0])):
        total = set()
        for row in range(len(land)):
            total.add(land[row][col])

        result = max(sum(map(lambda x: oils[x], total)), result)

    return result

