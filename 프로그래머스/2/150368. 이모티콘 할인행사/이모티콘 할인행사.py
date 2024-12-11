import sys
import math

sys.setrecursionlimit(10**9)

dd = [10, 20, 30, 40]


def allEmotions(n, li, result):
    if len(li) == n:
        result.append(li[:])
        return result

    for i in range(4):
        li.append(dd[i])
        result = allEmotions(n, li, result)
        li.pop()

    return result


def calc(user, emo, emoticons):
    sumv = 0
    hal, limi = user
    for i, e in enumerate(emo):
        if e < hal:
            continue
        sumv += math.floor(emoticons[i] * (100 - e) / 100)

    if sumv < limi:
        return [0, sumv]

    else:
        return [1, 0]


def getPlusValue(emo, users, emoticons):
    result = [0, 0]
    for user in users:
        a, b = calc(user, emo, emoticons)
        result[0] += a
        result[1] += b

    return result


def solution(users, emoticons):
    result = []
    for emo in allEmotions(len(emoticons), [], []):
        result.append(getPlusValue(emo, users, emoticons))

    result.sort()
    return result[-1]


