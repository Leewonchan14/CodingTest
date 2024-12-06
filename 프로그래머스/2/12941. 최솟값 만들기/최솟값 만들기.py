def solution(A,B):
    A.sort(reverse=True)
    B.sort()
    sum = 0
    while A and B:
        sum += A.pop() * B.pop()
        
    return sum