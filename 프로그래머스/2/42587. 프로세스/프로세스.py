from queue import PriorityQueue
from collections import deque

def solution(priorities, location):
    deq = deque([])
    que = PriorityQueue()
    for i,v in enumerate(priorities):
        que.put(( 1 / v, i))
        deq.append(( 1 / v, i))
        
    cnt = 0
    
    while True:
        if que.queue[0][0] != deq[0][0]:
            deq.append(deq.popleft())
            continue
        
        if que.queue[0][0] == deq[0][0]:
            cnt += 1
            if deq[0][1] == location:
                return cnt
            deq.popleft()
            que.get()
            
            
