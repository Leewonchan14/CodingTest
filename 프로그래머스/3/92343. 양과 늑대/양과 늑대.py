from collections import deque


def solution(info, edges):
    child = {i: [] for i in range(len(info))}

    for a, b in edges:
        child[a].append(b)

    def bfs():
        max_sheep_cnt = 0
        que = deque()
        que.append((1, 0, {0}))

        while que:
            sheep_cnt, wolf_cnt, nodes = que.popleft()

            if sheep_cnt <= wolf_cnt:
                continue

            max_sheep_cnt = max(max_sheep_cnt, sheep_cnt)
            for node in nodes:
                for next_node in child[node]:
                    if next_node in nodes:
                        continue

                    if info[next_node] == 1:
                        que.append((sheep_cnt, wolf_cnt + 1, nodes | {next_node}))
                    else:
                        que.append((sheep_cnt + 1, wolf_cnt, nodes | {next_node}))

        return max_sheep_cnt

    return bfs()
