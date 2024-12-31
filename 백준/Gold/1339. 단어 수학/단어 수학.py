import sys

input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
mapper = {}


def setMapper():
    global mapper
    dic = {}
    for i in range(-1, -max([len(a) for a in arr]) - 1, -1):
        for a in arr:
            if i < -len(a):
                continue
            dic[a[i]] = dic.get(a[i], 0) + (10 ** ((i * -1) - 1))

    sort_li = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)

    for i in range(9, 9 - len(sort_li), -1):
        mapper[sort_li[9 - i]] = i


def main():
    setMapper()
    sumv = 0
    for a in arr:
        sumv += int("".join([str(mapper[s]) for s in a]))

    return sumv


print(main())
