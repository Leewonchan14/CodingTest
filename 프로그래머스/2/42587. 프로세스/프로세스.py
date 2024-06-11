from collections import deque

def solution(priorities, location):
    cnt = 0
    que = deque(enumerate(priorities))
    li = sorted(priorities)
    
    while que:
        pop = que.popleft()
        if li and li[-1] == pop[1]:
            cnt+=1
            li.pop()
            
            if pop[0] == location:
                break
            
            continue
            
        que.append(pop)
        
    return cnt