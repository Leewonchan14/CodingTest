def key(x):
    a,b = x
    return (b - a , a)

def solution(sequence, k):
    l = 0
    r = 0
    nsum = 0
    result = []
    while True:
        if nsum < k and r >= len(sequence):
            break
        
        
        if nsum < k:
            nsum += sequence[r]
            r += 1
        elif nsum > k:
            nsum -= sequence[l]
            l += 1
        
        if nsum == k:
            result.append((l, r))
            nsum -= sequence[l]
            l += 1
            
    result.sort(key=key)
    return [result[0][0], result[0][1] - 1]
    