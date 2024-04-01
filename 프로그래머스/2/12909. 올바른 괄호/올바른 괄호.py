def solution(s):
    stk = []
    for i in s:
        if not stk or i == "(":
            stk.append(i)
            continue
        
        if stk[-1] == "(":
            stk.pop()
            continue
        else:
            return False
        
    return len(stk) == 0
        
        