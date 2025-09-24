import sys

input = sys.stdin.readline

k, n = [int(i) for i in input().split()]
dp = []
for _ in range(k):
    dp.append(int(input()))

left = 1
right = max(dp)
result = 0

while True:
    mid = (left + right) // 2
    cal = sum([i // mid for i in dp])

    if cal < n:
        right = mid - 1
    elif cal >= n:
        left = mid + 1
        result = mid

    if right < left:
        print(result)
        break
