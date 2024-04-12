import math
def solution(k, d):
    cnt = 2 * len(range(0, d + 1, k)) - 1
    for i in range(k, d, k):
        dx = math.floor((d ** 2 - i ** 2) ** 0.5)
        cnt += dx // k
    return cnt
