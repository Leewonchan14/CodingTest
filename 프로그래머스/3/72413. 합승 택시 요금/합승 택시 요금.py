def solution(n, s, a, b, fares):
    arr = [[float('inf')] * (n + 1)  for _ in range(n + 1)]
    
    for a1,b1,c1 in fares:
        arr[a1][b1] = c1
        arr[b1][a1] = c1
        
    for i in range(1, n + 1):
        arr[i][i] = 0
        
    for k in range(1, n + 1):
        for a1 in range(1, n + 1):
            for b1 in range(1, n + 1):
                arr[a1][b1] = min(arr[a1][b1], arr[a1][k] + arr[k][b1])
    
    minv = float('inf')
    for k in range(1, n + 1):
        minv = min(minv, arr[s][k] + arr[a][k] + arr[b][k])
        
    return minv