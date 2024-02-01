def solution(n, control):
    m = {"w": 1, "s": -1, "d" : 10, "a":-10}
    
    for i in control:
        n += m[i]
    return n