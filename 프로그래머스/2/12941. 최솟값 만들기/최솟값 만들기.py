def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    count = 0
    for i in range(len(A)):
        count += A[i] * B[i]
    return count
        
    

    