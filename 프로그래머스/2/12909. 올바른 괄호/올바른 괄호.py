def solution(s):
    li = list(s)
    stk = []
    for i in li:
        if i == "(":
            stk.append(i)
            continue
            
        # i == ")"
        if not stk or stk[-1] == ")":
            return False
        elif stk[-1] == "(":
            stk.pop()
            
        
    return len(stk) == 0
        