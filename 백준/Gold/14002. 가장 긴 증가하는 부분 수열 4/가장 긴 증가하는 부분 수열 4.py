import sys

input = sys.stdin.readline


def main(arr):
    dp = [[i] for i in arr]
    for i in range(len(arr)):
        pre = sorted(
            [dp[j] for j in range(i) if dp[j][-1] < arr[i]], key=lambda x: -len(x)
        )
        pre = pre[0] if pre else []
        dp[i] = [*pre, *dp[i]]

    dp.sort(key=lambda x: -len(x))

    print(len(dp[0]))
    print(" ".join([str(i) for i in dp[0]]))


input()

arr = [int(i) for i in input().split()]
main(arr)
