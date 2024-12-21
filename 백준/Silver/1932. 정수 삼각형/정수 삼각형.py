def main(arr):
    for r in range(1, len(arr)):
        arr[r][0] += arr[r - 1][0]
        for c in range(1, len(arr[r]) - 1):
            arr[r][c] += max(arr[r - 1][c - 1], arr[r - 1][c])              
        arr[r][-1] += arr[r - 1][-1]
        
    return max(arr[-1])

import sys

input = sys.stdin.readline

tc = int(input())
arr = [[int(i) for i in  input().split()] for _ in range(tc)]

print(main(arr))