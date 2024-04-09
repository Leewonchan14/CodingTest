from collections import deque

def gap3(a,b):
    return sum([1 if a[i] != b[i] else 0 for i in range(len(a))]) == 1

def bfs(begin, target, words):
    que = deque()
    que.append((begin, 0))
    while que:
        x, cnt = que.popleft()
        if x == target:
            return cnt
        
        if cnt >= len(words):
            return 0
        
        for w in words:
            if gap3(w, x):
                que.append((w, cnt + 1))
    return 0

def solution(begin, target, words):
    return bfs(begin, target, words)