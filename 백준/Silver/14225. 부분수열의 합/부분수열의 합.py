import sys

input = sys.stdin.readline

n = int(input())
arr = [int(i) for i in input().split()]

def main():
    li = []
    mask = [False] * (100000 * 20 + 1)
    def recur(sumv):
        if li:
            mask[sumv] = True
        if len(li) == n:
            return
        
        for i in range(len(arr)):
            if not li or i > li[-1]:
                li.append(i)
                recur(sumv + arr[i])
                li.pop()
    recur(0)
    i = 1
    while mask[i]:
        i += 1
        
    return i

print(main())