def _const(n):
    _n = str(n)
    _n = list(map(int, list(_n)))
    return n + sum(_n)
index = 1
n = int(input())
while True:
    _n = _const(index)
    if _n == n:
        print(index)
        break
    elif index > n:
        print(0)
        break
    else:
        index += 1
    
    
    