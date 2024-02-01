def solution(slice, n):
    return n /slice if n % slice == 0 else int(n / slice) + 1