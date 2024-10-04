from collections import deque

def is_one(start, end):
    if len(start) != len(end):
        return False
    
    return sum([1 if start[i] != end[i] else 0 for i in range(len(start))]) == 1

def bfs(visited, start, word, end):
    que = deque([(start, 0)])
    while que:
        item, k = que.popleft()
        
        if item == end:
            return k
        
        for w in word:
            if visited[w] or not is_one(item, w):
                continue
            visited[w] = True
            que.append((w, k + 1))
    
    return 0
    

def solution(begin, target, words):
    visited = {w: False for w in words}
    return bfs(visited, begin, words, target)