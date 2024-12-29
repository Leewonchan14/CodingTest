import sys

input = sys.stdin.readline

input()
arr = [int(i) for i in input().split()]

def main():
    visited = [False] * (10 ** 6 + 1)
    li = []
    def recur(sumv):
        if li and sumv < len(visited):
            visited[sumv] = True
            
        if len(li) == len(arr):
            return
        
        for i in range(len(arr)):
            if not li or i > li[-1]:
                li.append(i)
                recur(sumv + arr[i])
                li.pop()
                
    recur(0)
    for i in range(1, len(visited)):
        if not visited[i]:
            return i

print(main())