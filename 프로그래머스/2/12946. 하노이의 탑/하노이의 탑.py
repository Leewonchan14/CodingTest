import sys

sys.setrecursionlimit(10 ** 9)

def recursion(n, start, end, mid, li):
    if n == 1:
        li.append([start, end])
        return li
    
    li = recursion(n - 1, start, mid, end, li)
    li = recursion(1, start, end, mid, li)
    li = recursion(n - 1, mid, end, start, li)
    return li

def solution(n):
    return recursion(n, 1, 3, 2, [])