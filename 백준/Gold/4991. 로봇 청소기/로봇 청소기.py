import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_y, start_x, grid, n, m):
    """ grid에서 (start_y, start_x)로부터 모든 칸까지의 최단거리를 BFS로 구해 반환.
        도달 불가능한 칸은 -1
    """
    dist_map = [[-1]*m for _ in range(n)]
    dist_map[start_y][start_x] = 0
    q = deque([(start_y, start_x)])

    # 상하좌우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] != 'x' and dist_map[ny][nx] == -1:
                dist_map[ny][nx] = dist_map[y][x] + 1
                q.append((ny, nx))
    return dist_map


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break  # 종료 조건

    grid = []
    dirty_positions = []
    start_y = start_x = None

    for r in range(h):
        row = list(input().rstrip())
        grid.append(row)
        for c, val in enumerate(row):
            if val == 'o':
                start_y, start_x = r, c
            elif val == '*':
                dirty_positions.append((r, c))

    # (시작점 + 더러운칸) => 노드 목록
    nodes = [(start_y, start_x)] + dirty_positions
    node_count = len(nodes)  # 최대 1 + 10 = 11

    # 각 노드끼리의 최단거리 dist[i][j]
    dist = [[-1]*node_count for _ in range(node_count)]

    # BFS하여 dist 행렬 채우기
    for i, (sy, sx) in enumerate(nodes):
        dist_map = bfs(sy, sx, grid, h, w)
        for j, (ey, ex) in enumerate(nodes):
            dist[i][j] = dist_map[ey][ex]  # (sy,sx)->(ey,ex) 최단거리
        # dist_map이 -1인 경우도 있을 수 있음

    # 만약 어떤 노드 간 거리가 -1이면 => 로봇이 모든 더러운 칸 방문 불가능
    impossible = any(dist[i][j] == -1 for i in range(node_count)
                     for j in range(node_count) if i != j)
    if impossible:
        print(-1)
        continue

    # -- 비트마스크 TSP (node 0 = 로봇 시작, 나머지는 더러운칸) --
    # dp[mask][i] = 현재 방문집합이 mask이고, 마지막 위치가 i일 때 필요한 최단 거리
    from math import inf
    dp = [[inf]*node_count for _ in range(1 << node_count)]

    # 시작: node 0만 방문한 상태
    dp[1 << 0][0] = 0

    for mask in range(1 << node_count):
        for i in range(node_count):
            if dp[mask][i] == inf:
                continue
            # i를 현재 노드, mask는 이미 방문한 집합
            for j in range(node_count):
                if mask & (1 << j):  # 이미 방문
                    continue
                # i->j 거리 추가
                cost = dp[mask][i] + dist[i][j]
                nxt_mask = mask | (1 << j)
                if cost < dp[nxt_mask][j]:
                    dp[nxt_mask][j] = cost

    # 모든 dirty를 방문한 상태: mask = (1<<node_count)-1
    # node 0은 시작점이지만, 반드시 끝날 때 0으로 돌아갈 필요 없음
    answer = min(dp[(1 << node_count) - 1][i] for i in range(node_count))
    print(answer if answer != inf else -1)
