def main(n, _arr):
    arr = _arr[:]
    stk = [arr.pop()]
    while arr and arr[-1] > stk[-1]:
        stk.append(arr.pop())

    if not arr:
        return [-1]

    last = arr.pop()
    stk.append(last)
    stk.sort()
    lastN = last

    for a in stk:
        if a > last:
            lastN = a
            break

    return [*arr, *[lastN, *[s for s in stk if s != lastN]]]


import sys

input = sys.stdin.readline

n = int(input())
arr = [int(i) for i in input().split()]

print(" ".join([str(i) for i in main(n, arr)]))
