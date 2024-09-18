def is_collect(s):
    dic = {
        "{": "}",
        "[" : "]",
        "(" : ")",
        "}": "{",
        "]" : "[",
        ")" : "("
    }
    
    open = "{[("
    
    stk = []
    
    for v in s:
        if stk and v not in open and stk[-1] == dic[v]:
            stk.pop()
            continue
            
        stk.append(v)
        
    return len(stk) == 0
            
        


def solution(s):
    cnt = 0
    for i in range(len(s)):
        if (is_collect(s)):
            cnt += 1
        s = s[1:] + s[0]
            
    return cnt
            