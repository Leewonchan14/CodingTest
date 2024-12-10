def recursive(n):
    if n <= 3:
        return "4124"[n]
    
    nn = n // 3
    if n % 3 == 0:
        nn -= 1
        
    return recursive(nn) + "412"[n % 3]

def solution(n):
    return recursive(n)