_max = [0]

def recursive(k, dungeons, visited, c):
    _max[0] = max(_max[0], c)
    
    for i, d in enumerate(dungeons):
        if visited[i]:
            continue
            
        if k < d[0] or k < d[1]:
            continue
        
        visited[i] = True
        recursive(k - d[1], dungeons, visited, c + 1)
        visited[i] = False
        

def solution(k, dungeons):
    dungeons.sort(key=lambda x: x[1])
    visited = [False] * len(dungeons)
    recursive(k, dungeons, visited, 0)
    
    return _max[0]