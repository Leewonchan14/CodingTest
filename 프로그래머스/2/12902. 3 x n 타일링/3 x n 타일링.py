def solution(n):
    if n==2:
        return 3
    if n==4:
        return 11
    answer = 0
    n/=2
    n-=2
    c=(3,11)
    while n>0:
        c=(c[1],c[1]*4-c[0])
        n-=1
    return c[1]%1000000007