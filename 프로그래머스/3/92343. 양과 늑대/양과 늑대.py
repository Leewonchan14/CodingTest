def solution(info, edges):
    from collections import defaultdict, deque

    def bfs(info, graph):
        max_sheep = 0
        queue = deque([(0, 1, 0, [0])])

        while queue:
            node, sheep, wolf, route = queue.popleft()
            max_sheep = max(max_sheep, sheep)

            for next_node in route:
                for child in graph[next_node]:
                    if child not in route:
                        next_sheep = sheep + (info[child] == 0)
                        next_wolf = wolf + (info[child] == 1)

                        if next_wolf < next_sheep:
                            queue.append((child, next_sheep, next_wolf, route + [child]))

        return max_sheep

    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)

    return bfs(info, graph)

