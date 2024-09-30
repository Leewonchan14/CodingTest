import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

inputs = deque([int(input()) for _ in range(n)])
order = deque([i for i in range(1, n + 1)])


stk = []
result = []
flag = True

while order or inputs:
    while not stk or (order and stk and inputs and stk[-1] < inputs[0]):
        stk.append(order.popleft())
        result.append(1)
        
    while stk and inputs and stk[-1] == inputs[0]:
        stk.pop()
        inputs.popleft()
        result.append(0)
        
    if stk and inputs and stk[-1] > inputs[0]:
        flag = False
        break
    
        
            
if not flag:
    print("NO")
else: 
    print("\n".join(["+" if i == 1 else "-" for i in result]))
    
    
