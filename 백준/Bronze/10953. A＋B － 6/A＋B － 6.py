import sys

input = sys.stdin.readline

tc = int(input())

for ss in [input().split(",") for _ in range(tc)]:
    print(sum([int(j) for j in ss]))
