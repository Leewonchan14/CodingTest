def main(n, _arr):
    arr = _arr[:]
    stk = [arr.pop()]
    while arr and arr[-1] < stk[-1]:
        stk.append(arr.pop())
    
    if not arr:
        return [-1]
    
    last = arr.pop()
    stk.append(last)
    stk.sort(reverse=True)
    preLast = stk[stk.index(last) + 1]
    
    return [*arr, preLast, *[s for s in stk if s != preLast]]

import sys

input = sys.stdin.readline
n = int(input())
arr = [int(i) for i in input().split()]

print(" ".join([str(s) for s in main(n, arr)]))