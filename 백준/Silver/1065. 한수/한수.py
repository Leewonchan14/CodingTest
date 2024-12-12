import sys

input = sys.stdin.readline


def isHan(n):
    if n < 100:
        return True
    n = list(str(n))
    pre = int(n[0]) - int(n[1])
    for x in range(1, len(n) - 1):
        if pre != int(n[x]) - int(n[x + 1]):
            return False

    return True


print(sum([1 for i in range(1, int(input()) + 1) if isHan(i)]))
