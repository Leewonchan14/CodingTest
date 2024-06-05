from collections import deque

def solution(A, B):
    A.sort()
    B.sort()
    
    A = deque(A)
    B = deque(B)
    
    cnt = 0
    
    while A and B:
        if A[0] < B[0]:
            cnt += 1
            A.popleft()
            B.popleft()
        else :
            B.popleft()
    
    return cnt

print(solution([1,3,9,9], [2,2,8,10])) # 3나와야함