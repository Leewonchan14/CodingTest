def key(x):
    return ((x * 4)[:4], x)
        

def solution(numbers):
    return str(int("".join(sorted(list(map(str, numbers)), key=key, reverse=True))))
