import sys

input = sys.stdin.readline

stk = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        stk.pop()
        continue
    stk.append(n)
    
print(sum(stk))