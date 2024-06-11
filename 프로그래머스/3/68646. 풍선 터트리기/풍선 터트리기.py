def solution(a):
    minv = a[0]
    min_idx = 0
    for i, v in enumerate(a):
        if v < minv:
            min_idx = i
            minv = v
    
    li = []
    m = a[0]
    for i in range(min_idx + 1):
        if a[i] <= m:
            m = a[i]
            li.append(a[i])
            
    m = a[-1]
    for i in range(len(a) - 1, min_idx - 1, -1):
        if a[i] <= m:
            m = a[i]
            li.append(a[i])
            
    return len(set(li))
        