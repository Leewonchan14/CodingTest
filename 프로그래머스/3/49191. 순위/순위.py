def solution(n, results):
    arr = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for _i in range(1, n + 1):
        arr[_i][_i] = 0
    
    for a,b in results:
        arr[a][b] = 1
        arr[b][a] = -1
        
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                # a > k and k > b 라면 a > b 이다.
                if arr[a][k] == 1 and arr[k][b] == 1:
                    arr[a][b] = 1
                    arr[b][a] = -1
    
    cnt = 0
    for li in arr[1:]:
        if all([x != float('inf') for x in li[1:]] ):
            cnt += 1
            
    return cnt
        
        
    
        
    
    
        
    
    