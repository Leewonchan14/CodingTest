import math


def isAlpha(s):
    return ord("a") <= ord(s) <= ord("z") or ord("A") <= ord(s) <= ord("Z")


def counter(str1):
    dic = {}
    for i in range(len(str1) - 1):
        if isAlpha(str1[i]) and isAlpha(str1[i + 1]):
            s = str1[i].lower() + str1[i + 1].lower()
            dic[s] = dic.get(s, 0) + 1

    return dic


def 교(str1, str2):
    c1 = counter(str1)
    c2 = counter(str2)

    c3 = {}
    for k, _ in c1.items():
        if k in c2:
            c3[k] = min(c1[k], c2[k])

    return sum(c3.values())


def 합(str1, str2):
    c1 = counter(str1)
    c2 = counter(str2)

    for k in c2.keys():
        c1[k] = max(c1.get(k, 0), c2[k])

    return sum(c1.values())


def solution(str1, str2):
    a = 교(str1, str2)
    b = 합(str1, str2)
    return math.floor((a / b if b != 0 else 1) * 65536)
