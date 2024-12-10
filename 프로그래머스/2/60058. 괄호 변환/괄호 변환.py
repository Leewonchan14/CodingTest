def reverse(m):
    dic = {"(": ")", ")" : "("}
    return "".join([dic[i] for i in m])

def is_collect(m):
    stk = []
    for i in m:
        if i == ")":
            if not stk or stk[-1] != "(":
                return False
            stk.pop()
        else:
            stk.append(i)
            
    return len(stk) == 0

def to_collect(m):
    if is_collect(m):
        return m
    
    for i in range(1, len(m) + 1):
        u = m[0:i]
        if u.count("(") == u.count(")"):
            v = m[i:]
            if is_collect(u):
                return u + to_collect(v)
            
            return f"({to_collect(v)})" + reverse(u[1:-1])
            

def solution(p):
    return to_collect(p)