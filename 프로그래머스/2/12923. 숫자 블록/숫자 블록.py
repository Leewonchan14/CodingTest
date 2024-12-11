import math

def second(n):
    if n == 1:
        return 0
    if n <= 2:
        return 1
    
    result = []
    
    for i in range(2, int(n ** 0.5) + 1):
        d, m = divmod(n , i)
        if m == 0:
            if d <= 10 ** 7:
                return d
            else:
                result.append(i)
        
    return 1 if not result else result[-1]
        

def solution(begin, end):
    return [second(i) for i in range(begin, end + 1)]