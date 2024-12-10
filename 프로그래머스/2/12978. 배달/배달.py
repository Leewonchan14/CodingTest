from collections import defaultdict, deque

def solution(N, road, K):
    dic = defaultdict(list)
    for a,b,c in road:
        dic[a].append((b, c))
        dic[b].append((a, c))
        
    
    coasts = [float('inf')] * (N + 1)
    coasts[1] = 0
    que = deque([])
    que.append((1, 0))
    
    while que:
        n, coast = que.popleft()
        for nn, c in dic[n]:
            if c + coast <= coasts[nn]:
                coasts[nn] = c + coast
                que.append((nn, c + coast))
        
    return len([c for c in coasts if c <= K])
    
