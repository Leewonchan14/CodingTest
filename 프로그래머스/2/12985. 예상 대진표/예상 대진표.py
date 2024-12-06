import sys
import math
sys.setrecursionlimit(10 ** 9)

def recursive(a, b,  k):
    if a == b:
        return k
    
    return recursive(math.ceil(a / 2), math.ceil(b / 2), k + 1)

def solution(n,a,b):
    k = 1
    while a != b:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        k += 1
        
    return k - 1
        