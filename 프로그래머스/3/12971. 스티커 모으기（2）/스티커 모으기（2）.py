def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
    
    dp0 = sticker[:]
    dp0[1] = dp0[0]
    dp0[-1] = 0
    
    for i in range(2, len(sticker)):
        dp0[i] = max(dp0[i - 1] , dp0[i - 2] + dp0[i])
        
    dp1 = sticker[:]
    dp1[0] = 0
    
    for i in range(2, len(sticker)):
        dp1[i] = max(dp1[i - 1] , dp1[i - 2] + dp1[i])
        
    return max(dp0[-1], dp1[-1])
