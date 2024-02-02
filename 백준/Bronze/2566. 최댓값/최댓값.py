row,col = 0,0
__max = 0
for i in range(9):
    s = input().split()
    s = list(map(int, s))
    _max = max(s)
    if __max < _max:    
        __max = _max
        row, col = i, s.index(_max)
print(__max)
print(f"{row+1} {col+1}")