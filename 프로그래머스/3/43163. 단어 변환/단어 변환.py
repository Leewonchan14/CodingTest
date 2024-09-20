from collections import deque

def is_can_go(star, end):
    return sum([int(a != b) for a, b in zip(star, end)]) == 1
            
    return cnt == 1

def solution(begin, target, words):
    que = deque()
    
    visited = {w: False for w in words}
    
    visited[begin] = True
    
    que.append((begin, 0))
    
    while que:
        start, cnt = que.popleft()
        
        if start == target:
            return cnt
        
        for w in words:
            if not visited[w] and is_can_go(start, w):
                visited[w] = True
                que.append((w, cnt + 1))
                
    return 0
        