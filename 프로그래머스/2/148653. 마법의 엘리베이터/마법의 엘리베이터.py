def recursive(num):
    if num == 0:
        return 0
    
    n10 = num % 100 // 10
    n1 = num % 10
    
    if n1 < 5:
        return n1 + recursive(num // 10)
    
    if n1 > 5:
        return 10 - n1 + recursive(num // 10 + 1)
    
    if n1 == 5 and n10 >= 5:
        return 10 - n1 + recursive(num // 10 + 1)
    
    if n1 == 5 and n10 < 5:
        return n1 + recursive(num // 10)
    
    

def solution(storey):
    return recursive(storey)