from collections import deque

def solution(number, k):
    stk = []
    for i in number:
        while stk and k > 0 and stk[-1] < i:
            stk.pop()
            k -= 1
        
        stk.append(i)
        
    if k > 0:
        stk = stk[:-k]
        
    return str(int("".join(stk)))
    
        
    