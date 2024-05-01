def solution(n, s):
    if n > s:
        return [-1]
    
    result = [s // n for _ in range(n)]
    div = s % n
    for i in range(n - div, n):
        result[i] += 1
    return result
    