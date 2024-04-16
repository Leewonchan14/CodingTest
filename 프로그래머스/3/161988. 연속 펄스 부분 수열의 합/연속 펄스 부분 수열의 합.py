def solve(sequence):
    length = len(sequence)
    dp = [0 for _ in range(length)]
    dp[0] = sequence[0]
    for i in range(1, length):
        dp[i] = max(dp[i - 1] + sequence[i], sequence[i])
        
    dp.sort()
    return dp[-1]
    

def solution(sequence):
    length = len(sequence)
    a = [(-1 if i % 2 == 0 else 1) * sequence[i] for i in range(length)]
    b = [(-1 if i % 2 != 0 else 1) * sequence[i] for i in range(length)]
    return max(solve(a), solve(b))