def solution(s):
    stk = []
    for _s in s:
        if len(stk) == 0:
            stk.append(_s)
            continue
        
        if _s == ")":
            if stk[-1] == "(":
                stk.pop()
                continue
            else :
                break
                
        stk.append(_s)
    print(stk)
    return len(stk) == 0