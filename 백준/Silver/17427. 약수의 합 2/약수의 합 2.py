import math, sys


def recur(n):
    return sum([i * (n // i) for i in range(1, n + 1)])


print(recur(int(input())))
