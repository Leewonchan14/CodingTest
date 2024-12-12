dp = {}


def fibo(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    if n not in dp:
        dp[n] = fibo(n - 1) + fibo(n - 2)

    return dp[n]


print(fibo(int(input())))
