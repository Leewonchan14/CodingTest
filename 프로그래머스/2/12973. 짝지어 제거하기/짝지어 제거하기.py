def solution(s):
    stk = []
    for i in s:
        if not stk or stk[-1] != i:
            stk.append(i)
            continue
        
        stk.pop()
        
    return 0 if stk else 1
            
        