from sys import stdin

# n = 5
n = int(input())
li = [int(stdin.readline().rstrip()) for _ in range(n)]
# li = [10, 15, 20, 24, 52]


li.sort(reverse=True)

index = 0
_max = 0
while index < n:
    weight = li[index] * (index + 1)
    if weight > _max:
        _max = weight
    index += 1

print(_max)
