from collections import deque

def solution(cacheSize, cities):
    cache = deque([])
    runtime = 0
    for c in cities:
        c = c.lower()
        if c not in cache:
            runtime += 5
            if cacheSize == 0:
                continue
                
            cache.append(c)
            if len(cache) > cacheSize:
                cache.popleft()
                
            
        else:
            runtime += 1
            cache.remove(c)
            cache.append(c)
            
    return runtime