import sys
sys.setrecursionlimit(10 ** 8) 

input = sys.stdin.readline

n = int(input())

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def main(dp):
    visited = set()
    def recur(y, x):
        visited.add((y, x))
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < len(dp) and 0 <= nx < len(dp[0]) and dp[ny][nx] == 1 and (ny, nx) not in visited:
                recur(ny, nx)        
    
    cnt = 0
    for y in range(len(dp)):
        for x in range(len(dp[0])):
            if (y, x) not in visited and dp[y][x] == 1:
                cnt += 1
                recur(y, x)
    
    return cnt
            


for _ in range(n):
    x, y, k = [int(i) for i in input().split()]
    dp = [[0] * x for _ in range(y)]
    for _ in range(k):
        x,y = [int(i) for i in input().split()]
        dp[y][x] = 1
        
    print(main(dp))
        
