import itertools
from collections import deque

pick_name = ["diamond", "iron", "stone"]
vocab = {name: index for index, name in enumerate(pick_name)}
vocab["diamond"] = 0
firo = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]


def mapper(mine: list):
    return list(map(mine.count, ["diamond", "iron", "stone"]))


def solution(picks, minerals):
    # 광물을 5개씩 묶고 곡괭이 갯수만큼만 가져온다.
    minerals = [minerals[i:i + 5] for i in range(0, len(minerals), 5)][:sum(picks)]

    # [diamond, iron, stone] 각 갯수만큼으로 map 한다.
    minerals = list(map(mapper, minerals))

    # diamond, iron, stone 갯수로 정렬한다. (다이아, 철, 돌 많이 가지고 있는거 순)
    minerals.sort(reverse=True)

    firo_sum = 0

    # 다이아를 먼저 다 쓰고, 철, 돌 곡괭이 순서대로 다 사용한다.
    for mine in minerals:
        idx = 0
        # diamond 사용
        if picks[0] > 0:
            picks[0] -= 1
            idx = 0
        elif picks[1] > 0:
            picks[1] -= 1
            idx = 1
        elif picks[2] > 0:
            idx = 2

        firo_sum += sum(firo[idx][index] * m for index, m in enumerate(mine))

    return firo_sum