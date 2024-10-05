def solution(N, road, K):
    l = [[float('inf')] * (N + 1) for i in range(N + 1)]
        
    for a,b,c in road:
        l[a][b] = min(l[a][b], c)
        l[b][a] = min(l[b][a], c)
        
    for i in range(1, N + 1):
        l[i][i] = 0
        
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                l[a][b] = min(l[a][b], l[a][k] + l[k][b])
                
    return len([i for i in l[1] if i <= K])