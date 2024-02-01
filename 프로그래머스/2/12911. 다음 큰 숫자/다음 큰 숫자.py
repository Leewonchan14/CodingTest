def solution(n):
    target = bin(n)[2:].count("1")
    n += 1
    bi = bin(n)[2:]
    while bi.count("1") != target:
        n += 1
        bi = bin(n)[2:]
    
    return n
        
    
    