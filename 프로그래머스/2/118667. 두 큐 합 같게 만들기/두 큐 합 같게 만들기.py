from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2= sum(queue2)
    que1 = deque(queue1)
    que2 = deque(queue2)
    
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    mid = (sum1 + sum2) // 2
    
    cnt = 0
    i = (len(que1) + len(que2)) * 2
    
    while (sum1 != mid or sum2 != mid) and i > -1:
        if sum1 > sum2:
            pop = que1.popleft()
            que2.append(pop)
            sum1 -= pop
            sum2 += pop
            
        else:
            pop = que2.popleft()
            que1.append(pop)
            sum2 -= pop
            sum1 += pop    
            
        i -= 1
        cnt += 1
        
        
    if i < 0:
        return -1
    
    
    return cnt
    