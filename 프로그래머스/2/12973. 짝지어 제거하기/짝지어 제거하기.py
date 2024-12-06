import sys
sys.setrecursionlimit(10 ** 9)

def recursive(s):
    if not s:
        return True
    
    stk = []
    isNothing = True
    for i, c in enumerate(s):
        if not stk:
            stk.append(c)
            continue
        
        if stk[-1] == c:
            isNothing = False
            stk.pop()
            continue
            
        stk.append(c)
    
    if isNothing:
        return False
    
    return recursive(stk)

def solution(s):
    return int(recursive(list(s)))