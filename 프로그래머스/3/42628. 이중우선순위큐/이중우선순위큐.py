import sys
from collections import deque


def find_index(li, value):
    left = 0
    right = len(li)

    while left < right:
        mid = (left + right) // 2
        if value < li[mid]:
            right = mid
        elif value > li[mid]:
            left = mid + 1
        else:
            return mid

    return left


def solution(operations):
    li = deque()
    for i in operations:
        op, v = i.split()
        v = int(v)
        if op == "I":
            li.insert(find_index(li, v), v)

        elif op == "D":
            if v == -1 and li:
                li.popleft()
            elif v == 1 and li:
                li.pop()

    return [li[-1], li[0]] if li else [0, 0]

