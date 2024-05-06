from collections import deque
def solution(N, road, K):
    weight = [float('inf')] * (N + 1)
    dic = {i + 1 :[] for i in range(N)}
    for a, b, c in road:
        dic[a].append((c, b))
        dic[b].append((c, a))
        
    que = deque()
    que.append(1)
    weight[1] = 0
    
    while que:
        node = que.popleft()
        for w, n in dic[node]:
            if weight[node] + w < weight[n]:
                weight[n] = weight[node] + w
                que.append(n)
        
    return len([f for f in weight if f <= K])
    
        
    
        