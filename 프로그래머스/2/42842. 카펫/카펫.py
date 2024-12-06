import math
import sys
sys.setrecursionlimit(10 ** 9)

def recursive(k, yellow, brown):
    if yellow % k == 0 and 2 * ((yellow // k) + k) + 4 == brown:
        return k
    
    return recursive(k + 1, yellow, brown)
    
def solution(brown, yellow):
    k = recursive(math.ceil(math.sqrt(yellow)), yellow, brown)
    return [k + 2, yellow // k + 2]