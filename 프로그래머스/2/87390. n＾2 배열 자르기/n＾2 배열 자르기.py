def getPositionValue(k, n):
    row = k // n
    col = k % n
    
    return col if col >= row else row


def solution(n, left, right):
    return [getPositionValue(i ,n) + 1 for i in range(left, right + 1)]
    