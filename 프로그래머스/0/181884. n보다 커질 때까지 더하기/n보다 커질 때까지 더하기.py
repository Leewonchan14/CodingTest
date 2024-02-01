def solution(numbers, n):
    sumC = 0
    for i in numbers:
        sumC += i
        if sumC > n:
            break
            
    return sumC