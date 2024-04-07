def move(n, start, end, other, ls):
    if n == 1:
        ls.append([start,end])
        return
    
    move(n - 1, start, other, end, ls)
    move(1, start, end, other, ls)
    move(n - 1, other, end, start, ls)

def solution(n):
    ls = []
    move(n, 1, 3, 2, ls)
    return ls