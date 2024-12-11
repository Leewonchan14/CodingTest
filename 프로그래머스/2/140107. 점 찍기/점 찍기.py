import math

def solution(k, d):
    cnt = 0
    for i in range(k, d, k):
        sq = math.sqrt(d ** 2 - i ** 2)
        key = math.floor(sq)
        cnt += key // k
        
    return 2 * (d // k) + 1 + cnt