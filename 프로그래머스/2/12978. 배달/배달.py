from queue import PriorityQueue
def solution(N, road, K):
    dic = {i + 1 : [] for i in range(N)}
    for a,b,c in road:
        dic[a].append((c,b))
        dic[b].append((c,a))
        
    weights = [float('inf')] * (N + 1)
    weights[1] = 0
    que = PriorityQueue()
    
    que.put((0, 1))
    
    while que.queue:
        p_w, n = que.get()
        for next_w, next_node in dic[n]:
            if p_w + next_w >= weights[next_node]:
                continue
                
            weights[next_node] = p_w + next_w
            que.put((p_w + next_w, next_node))
    
    return len([w for w in weights if w <= K])
