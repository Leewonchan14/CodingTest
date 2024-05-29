def solution(k, ranges):
    dp = [0]
    while k != 1:
        nk = (k * 3 + 1) if k % 2 == 1 else k // 2
        area = nk + k
        dp.append((dp[-1] + area) if dp else area)
        k = nk
        
    r = []
    for a, b in ranges:
        if len(dp) - 1 + b < a:
            r.append(-1)
            continue
        r.append((dp[len(dp) - 1 + b] - dp[a]) / 2)
    return r