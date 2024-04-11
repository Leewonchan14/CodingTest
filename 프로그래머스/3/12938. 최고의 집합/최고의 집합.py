def solution(n, s):
    if s // n == 0:
        return [-1]
    
    length = s // n
    
    ls = [length] * n
    for i in range(-1, -(s % n) - 1, - 1):
        ls[i] += 1
    
    return ls