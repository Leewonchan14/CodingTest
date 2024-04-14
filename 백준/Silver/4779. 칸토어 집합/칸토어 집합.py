import sys

input = sys.stdin.readline


def recur(st, left, right):
    third = len(st) // 3
    if third == 0:
        return "-"

    if third == 1:
        return "- -"
    a = recur(st[:third], left, third)
    b = " " * third
    c = recur(st[:third], third * 2 + 1, right)
    return a + b + c


while True:
    try:
        N = int(input())
    except:
        break
    s = "-" * (3 ** N)
    print(recur(s, 0, len(s) - 1))


