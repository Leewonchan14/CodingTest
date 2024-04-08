import itertools

from collections import deque

def bfs(visited, linked, begin, target):
    que = deque()
    count = 0
    que.append((begin, count))
    while que:
        item, count = que.popleft()
        if item == target:
            return count
        
        for link in linked[item]:
            if not visited[link]:
                visited[link] = True
                que.append((link, count + 1))
    
    return 0
    

def is_one_gap(a,b):
    index = 0
    count = 0
    while index < len(a):
        if a[index] != b[index]:
            count += 1
        index += 1
        
    return count == 1

def solution(begin, target, words):
    linked = {begin : []}
    visited = {}
    
    for w in words:
        visited[w] = False
        if is_one_gap(begin, w):
            linked[begin].append(w)
    
    for a,b in itertools.combinations(words, 2):
        if is_one_gap(a,b):
            linked[a] = linked.get(a, [])
            linked[a].append(b)
            
            linked[b] = linked.get(b, [])
            linked[b].append(a)
            
    return bfs(visited, linked, begin, target)
            
    