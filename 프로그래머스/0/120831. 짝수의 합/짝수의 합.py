def solution(n):
    if n == 0:
        return 0
    
    if  2<= n <= 3:
        return 2
    
    n = n / 2 if n % 2== 0 else (n - 1) / 2
    
    return n**2 + n
    