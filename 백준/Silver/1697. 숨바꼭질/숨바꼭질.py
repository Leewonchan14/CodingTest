import sys
from collections import deque

def get_d(x):
    return [-1, 1, +x]


def main(n, k):
    visited = [False] * (10 ** 5 + 1)
    visited[n] = True
    
    que = deque([(n, 0)])
    
    while que:
        s, cnt = que.popleft()
        
        if s == k:
            return cnt
        
        for d in get_d(s):
            nn = s + d
            
            if 0 <= nn < len(visited) and not visited[nn]:
                visited[nn] = True
                que.append((nn, cnt + 1))
        
    

input = sys.stdin.readline

n,k = map(int, input().split())
print(main(n,k))