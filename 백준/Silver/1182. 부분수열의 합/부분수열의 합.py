import sys

input = sys.stdin.readline
_, s = map(int, input().split())
arr = [int(i) for i in input().split()]

def combi(n, k):
    li = []
    cnt = 0
    
    def recur(sumv):
        nonlocal cnt
        if li and sumv == s:
            cnt += 1
        if len(li) == k:
            return;
        
        for i in range(n):
            if not li or i > li[-1]:
                li.append(i)
                recur(sumv + arr[i])
                li.pop()
                
    recur(0)
    return cnt

def main():
    cnt = combi(len(arr), len(arr))
    return cnt

print(main())
    