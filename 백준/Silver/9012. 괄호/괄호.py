import sys

input = sys.stdin.readline

inputs = [input().strip() for _ in range(int(input()))]

def isCorrect(li):
    stk = []
    for i in li:
        if i == ")":
            if not stk or stk[-1] != "(":
                return False
            
            stk.pop()
            continue
            
        stk.append(i)
        
    return not stk
        

for i in inputs:
    li = list(i)
    print("YES" if isCorrect(li) else "NO")
