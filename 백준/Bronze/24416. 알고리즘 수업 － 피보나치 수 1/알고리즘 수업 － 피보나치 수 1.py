import sys

input = sys.stdin.readline

n = int(input())

cnt = [0]

dp = [1, 1]

for i in range(3, n + 1):
    cnt[0] += 1
    dp.append(dp[-1] + dp[-2])

print(dp[-1], cnt[0])
