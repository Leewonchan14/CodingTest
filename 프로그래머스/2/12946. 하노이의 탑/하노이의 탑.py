answer = []

def move(start, end, other, n):
    if n == 1:
        answer.append([start,end])
        return
    
    move(start, other, end, n - 1)
    move(start, end, other, 1)
    move(other, end, start, n - 1)

def solution(n):
    move(1, 3, 2, n)
    return answer