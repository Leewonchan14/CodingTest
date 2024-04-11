def solution(A, B):
    A.sort()
    B.sort()
    cnt = 0
    a_i = 0
    b_i = 0
    while b_i < len(B):
        if A[a_i] < B[b_i]:
            cnt += 1
            a_i += 1
            b_i += 1
        else:
            b_i += 1
            
    return cnt
    