# n = 200
n = int(input())
_sum = 0
i = 1
while True:
    _sum += i
    if _sum > n:
        break
    i += 1


print(i - 1)