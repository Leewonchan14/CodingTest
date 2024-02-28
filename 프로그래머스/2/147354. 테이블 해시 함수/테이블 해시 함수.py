def solution(data, col, row_begin, row_end):
    data.sort(key=lambda d: (d[col - 1], -d[0]))
    
    data = data[row_begin - 1:row_end]
    
    S_I = [sum(c % (i+row_begin) for c in row) for i, row in enumerate(data)]
    
    first = -1
    
    for i, s_i in enumerate(S_I) :
        if i == 0:
            first = s_i
            continue
        
        first = first ^ s_i
    
    return first
    
    
    
    
    