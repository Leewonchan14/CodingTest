def main(n, maps):
    minv = float('inf')
    li = []
    visited = [False] * (n + 1)
    def recur(sumv):
        nonlocal minv
        if len(li) == n:
            if maps[li[-1]][li[0]] != 0:
                minv = min(minv, sumv + maps[li[-1]][li[0]])
            return
        
        for i in range(n):
            if visited[i]:
                continue
                
            if not li or maps[li[-1]][i] != 0:
                weight = maps[li[-1]][i] if li else 0
                visited[i] = True
                li.append(i)
                recur(sumv + weight)
                li.pop()
                visited[i] = False
                
    recur(0)
    return minv
        

import sys

input = sys.stdin.readline

n = int(input())
maps = [[int(i) for i in input().split()] for _ in range(n)]
print(main(n, maps))