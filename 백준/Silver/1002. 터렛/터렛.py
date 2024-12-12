import math
import sys

input = sys.stdin.readline


def main(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심 간 거리 계산
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # 동일한 중심
    if dist == 0:
        if r1 == r2:
            return -1  # 무한한 교점
        else:
            return 0  # 교점 없음

    # 외접 또는 내접 (접점이 1개)
    if dist == r1 + r2 or dist == abs(r1 - r2):
        return 1

    # 두 점에서 만나는 경우
    if abs(r1 - r2) < dist < r1 + r2:
        return 2

    # 교점이 없는 경우
    return 0


tc = int(input())
li = [list(map(int, input().split())) for _ in range(tc)]
for l in li:
    print(main(*l))
