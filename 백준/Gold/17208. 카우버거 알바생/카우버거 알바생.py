import sys

input = sys.stdin.readline

n, m, k, = map(int, input().split())

li = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[[-1] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]


def knapsack(index, c, g):
    if index >= n:
        return 0

    if dp[index][c][g] != -1:
        return dp[index][c][g]

    n_c, n_g = li[index]

    choose, no_choose = 0, 0

    # index 주문이 가능 하다면 index 주문을 주문 했을 때 경우의 수
    if c - n_c >= 0 and g - n_g >= 0:
        choose = knapsack(index + 1, c - n_c, g - n_g) + 1

    # index 주문 안 받았을 때 경우의 수
    no_choose = knapsack(index + 1, c, g)

    # index개 까지 주문을 봤을때 남은 치즈 c, 남은 감튀 g개 일때 받은 주문의 최댓값
    dp[index][c][g] = max(choose, no_choose)

    return dp[index][c][g]


print(knapsack(0, m, k))
