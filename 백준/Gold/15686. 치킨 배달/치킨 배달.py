import sys
import itertools
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

chicken = {}
house = {}
for y in range(n):
    for x in range(n):
        if arr[y][x] == 2:
            chicken[(y, x)] = True
        elif arr[y][x] == 1:
            house[(y, x)] = float('inf')

min_value = float('inf')

for li in itertools.combinations(chicken.keys(), m):
    new_house = {}
    for h_y, h_x in house.keys():
        for c_y, c_x in li:
            new_house[(h_y, h_x)] = min(abs(h_y - c_y) + abs(h_x - c_x), new_house.get((h_y, h_x), float('inf')))

    min_value = min(min_value, sum(new_house.values()))

print(min_value)
