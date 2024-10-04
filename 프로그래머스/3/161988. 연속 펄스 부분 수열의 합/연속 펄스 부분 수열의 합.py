def solution(sequence):
    purse1 = [1 if i % 2 == 0 else -1 for i in range(len(sequence))]
    purse2 = [-1 if i % 2 == 0 else 1 for i in range(len(sequence))]
    
    dp1 = list(map(lambda x: x[0] * x[1], zip(sequence, purse1)))
    dp2 = list(map(lambda x: x[0] * x[1], zip(sequence, purse2)))
    
    for i in range(1, len(sequence)):
        dp1[i] = max(dp1[i - 1]+dp1[i], dp1[i])
        
    for i in range(1, len(sequence)):
        dp2[i] = max(dp2[i - 1]+dp2[i], dp2[i])
        
    
        
    return max(max(dp1), max(dp2))
    
