from queue import PriorityQueue
from collections import deque

def solution(priorities, location):
    pr = PriorityQueue()
    que = deque()
    for i,p in enumerate(priorities):
        pr.put((-p, p))
        que.append((p,i))
        
    cnt = 0
        
    while que:
        task, i = que.popleft()
        if pr.queue:
            if pr.queue[0][1] > task:
                que.append((task, i))
            else:
                pr.get()
                cnt += 1
                if i == location:
                    return cnt
        
        
    
        
    
    
    
    