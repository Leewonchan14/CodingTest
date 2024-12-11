import math


def sqrt(r, x):
    if r <= x:
        return 0

    return math.sqrt(r**2 - x**2)


def solution(r1, r2):
    sumv = 0
    for x in range(r2 + 1):
        a = math.ceil(sqrt(r1, x))
        b = math.floor(sqrt(r2, x))
        sumv += (b - a) + 1

    return (sumv - (r2 - r1 + 1)) * 4


