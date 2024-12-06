def recursive(n, oneCnt):
    if bin(n)[2:].count("1") == oneCnt:
        return n
    
    return recursive(n + 1, oneCnt)

def solution(n):
    return recursive(n + 1, bin(n).count("1"))