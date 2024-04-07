def is_collect(s):
    stk = []
    mapper = dict(zip(")}]({[", "({[)}]"))
    open = "({["
    close = ")}]"
    
    for i in s:
        if i in open or not stk:
            stk.append(i)
            continue
        
        if stk[-1] == mapper[i]:
            stk.pop()
            
    return len(stk) == 0
            
        


def solution(s):
    ls = [s[i:] + s[:i] for i in range(len(s))]
    return len([i for i in ls if is_collect(i)])
            