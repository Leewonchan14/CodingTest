import heapq

def dijkstra(start, relation, k):
    distances = [float('inf')] * (len(relation) + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
            
        for adj_distance, adj_node in relation[current_node]:
            distance = current_distance + adj_distance
            
            if distance < distances[adj_node]:
                distances[adj_node] = distance
                heapq.heappush(queue, (distance, adj_node))
    
    return len([d for d in distances if d <= k])

def solution(N, road, K):
    relation = {i: [] for i in range(1, N + 1)}
    
    for a, b, weight in road:
        relation[a].append((weight, b))
        relation[b].append((weight, a))
    
    return dijkstra(1, relation, K)

# 테스트
# print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3
