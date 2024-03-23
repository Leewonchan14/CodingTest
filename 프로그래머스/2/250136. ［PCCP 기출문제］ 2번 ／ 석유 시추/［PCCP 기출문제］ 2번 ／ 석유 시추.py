from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])

    isGo = [[False for _ in range(m)] for _ in range(n)]
    oils = {0: 0}

    que = deque()

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row in range(n):
        for col in range(m):
            # 갔다면 continue
            if isGo[row][col]:
                continue

            # 빈땅이면 continue
            if land[row][col] == 0:
                continue

            # 안가고 석유라면 Enque
            count = 0
            index = len(oils)

            isGo[row][col] = True
            land[row][col] = index
            que.append((row, col))

            while len(que) > 0:
                _row, _col = que.popleft()
                count += 1

                for dx, dy in direction:
                    n_row = _row + dx
                    n_col = _col + dy

                    # 땅을 넘으면
                    if n_row >= n or n_row < 0 or n_col >= m or n_col < 0:
                        continue

                    # 빈땅이면 continue
                    if land[n_row][n_col] == 0:
                        continue

                    # 안가면 Enque
                    if not isGo[n_row][n_col]:
                        land[n_row][n_col] = index
                        isGo[n_row][n_col] = True
                        que.append((n_row, n_col))

            oils[index] = count

    result = []

    for col in range(m):
        total = set()
        for row in range(n):
            total.add(land[row][col])
        result.append(sum(map(lambda x: oils[x], total)))

    return max(result)