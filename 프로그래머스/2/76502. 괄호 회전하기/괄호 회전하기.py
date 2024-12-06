match = {}
for i in ["()", "{}", "[]"]:
    a,b = list(i)
    match[b] = a
    
def isCorrect(s):
    stk = []
    for i in s:
        if not stk or i in match.values():
            stk.append(i)
            continue
            
        if i in match.keys() and match[i] == stk[-1]:
            stk.pop()
        else:
            return False
        
    return len(stk) == 0
        
                

def solution(s):
    cnt = 0
    for i in range(len(s)):
        _s = s[i:] + s[:i]
        if isCorrect(list(_s)):
            cnt += 1
            
    return cnt