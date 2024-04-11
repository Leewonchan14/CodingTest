from collections import deque
def bfs(start, visited, dic):
    que = deque()
    visited[start] = True
    que.append((start, 0))
    
    c_dic = {}
    
    while que:
        start, cnt = que.popleft()
        c_dic[cnt] = c_dic.get(cnt, 0) + 1
        for n in dic[start]:
            if not visited[n]:
                visited[n] = True
                que.append((n, cnt + 1))
                
    return sorted(c_dic.items())[-1][1]
    
def solution(n, edge):
    dic = {}
    visited = {}
    for a,b in edge:
        visited[a] = False
        dic[a] = dic.get(a, [])
        dic[a].append(b)
        
        visited[b] = False
        dic[b] = dic.get(b, [])
        dic[b].append(a)
        
    return bfs(1, visited, dic)