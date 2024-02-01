def isPrime(v):
    if v == 1:
        return True
    if v == 2:
        return True
    if v == 3:
        return True
    
    for i in range(2,int(v**0.5) + 1):
        if v % i == 0:
            return False
        
    return True

def solution(n):
    return len([i for i in range(1,n + 1) if not isPrime(i)])
    