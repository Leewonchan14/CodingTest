from collections import deque

def isGap3(a,b):
    if len(a) != len(b):
        return False
    
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
            if cnt >= 2:
                return False
    
    if cnt == 1:
        return True
    else:
        return False
        

def solution(begin, target, words):
    words.append(begin)
    dic = {w: [] for w in words}
    for i in range(len(words) - 1):
        for j in range(i, len(words)):
            if isGap3(words[i], words[j]):
                dic[words[i]].append(words[j])
                dic[words[j]].append(words[i])
                
    visited = {w : False for w in words}
    que = deque([(begin, 0)])
    while que:
        s,cnt = que.popleft()
        if s == target:
            return cnt
        
        for e in dic.get(s, []):
            if visited[e]:
                continue
            visited[e] = True
            que.append((e, cnt + 1))
            
    return 0
        