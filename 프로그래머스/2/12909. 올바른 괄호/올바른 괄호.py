def solution(s):
    stk = []
    for i in s:
        if not stk or i == "(":
            stk.append(i)
            continue
            
        if stk and stk[-1] == "(" and i == ")":
            stk.pop()
            
    return len(stk) == 0
            
            
        
        