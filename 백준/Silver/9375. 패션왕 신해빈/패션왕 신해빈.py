import sys

input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    dic = {}
    for a, b in [input().split() for j in range(int(input()))]:
        dic[b] = dic.get(b, 0) + 1

    mul = 1
    for m in dic.values():
        mul *= m + 1
    print(mul - 1)
