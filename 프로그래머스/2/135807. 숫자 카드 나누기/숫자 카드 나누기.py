from collections import deque
import math


def yack(n):
    que = deque([])
    i = math.ceil(math.sqrt(n))
    if i == math.sqrt(n):
        que.append(i)
    i -= 1
    while i > 0:
        if n % i == 0:
            que.appendleft(i)
            que.append(n // i)
        i -= 1

    return que


def sol(arrA, arrB):
    aGcd = arrA[0]
    for a in arrA:
        aGcd = math.gcd(a, aGcd)

    maxv = 0
    for ay in yack(aGcd):
        if not any(b % ay == 0 for b in arrB):
            maxv = max(maxv, ay)

    return maxv


def solution(arrayA, arrayB):
    a = sol(arrayA, arrayB)
    b = sol(arrayB, arrayA)
    return max(a, b)


# solution([10, 17], [5, 20])
