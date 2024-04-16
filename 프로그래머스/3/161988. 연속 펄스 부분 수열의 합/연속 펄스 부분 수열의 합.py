def solve(li):
    length = len(li)
    dp = [0 for _ in range(length)]
    dp[0] = li[0]
    for i in range(1,length):
        if dp[i - 1] >= 0:
            dp[i] = dp[i - 1] + li[i]
        elif dp[i - 1] < 0:
            dp[i] = li[i]
            
    dp.sort()
    return dp[-1]
        
        



def solution(sequence):
    length = len(sequence)
    a = [(-1 if i % 2 == 0 else 1) * sequence[i] for i in range(length)]
    b = [(-1 if i % 2 != 0 else 1) * sequence[i] for i in range(length)]
    return max(solve(a), solve(b))


