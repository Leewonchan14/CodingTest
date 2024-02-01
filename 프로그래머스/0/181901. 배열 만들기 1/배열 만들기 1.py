def solution(n, k):
    return list(filter(lambda v : v % k == 0, range(1,n+1)))