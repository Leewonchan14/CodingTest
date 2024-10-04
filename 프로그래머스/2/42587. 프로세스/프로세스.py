from collections import deque
from queue import PriorityQueue

def solution(priorities, location):
    p_que = PriorityQueue()
    
    for p in priorities:
        p_que.put((1 / p, p))
        
    que = deque(enumerate(priorities))
    
    cnt = 0
    
    while que[0][0] != location or que[0][1] != p_que.queue[0][1]:
        if que[0][1] == p_que.queue[0][1]:
            cnt += 1
            p_que.get()
            que.popleft()
            continue
            
        que.append(que.popleft())
        
    return cnt + 1