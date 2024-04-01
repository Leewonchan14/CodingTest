def solution(n):
    dp = [0,1,2]
    for i in range(3, n):
        dp.append((dp[-1] + dp[-2]) % 1234567)
        
    return dp[-1]
    