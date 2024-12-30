import sys

input = sys.stdin.readline

n = int(input())
arr = [int(i) for i in input().split()]


def main():
    visited = [False] * len(arr)
    maxv = -float('inf')
    def recur(sumv, cnt):
        nonlocal maxv
        if cnt == len(arr) - 2:
            maxv = max(maxv, sumv)
            return
        
        for i in range(1, len(arr) - 1):
            if not visited[i]:
                left = i - 1
                while visited[left]:
                    left -= 1
                right = i + 1
                while visited[right]:
                    right += 1
                    
                visited[i] = True
                recur(sumv + arr[left] * arr[right], cnt + 1)
                visited[i] = False
    
    recur(0, 0)
    return maxv


print(main())