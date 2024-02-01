def mapper(value):
    if value >= 50 and value % 2 == 0: 
        return value // 2
    elif value < 50 and value % 2 == 1: 
        return value * 2
    return value

def solution(arr):
    return list(map(mapper, arr))
