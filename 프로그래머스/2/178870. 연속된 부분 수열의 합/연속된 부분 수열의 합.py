def solution(sequence, k):
    start_index = 0
    end_index = 0
    sumv = sequence[0]
    ls = []
    while True:
        if sumv < k: 
            end_index += 1
            if end_index >= len(sequence):
                break
            sumv += sequence[end_index]
            
        elif sumv > k:
            if start_index >= len(sequence):
                break
            sumv -= sequence[start_index]
            start_index += 1
            
        if sumv == k:
            ls.append((start_index, end_index))
            sumv -= sequence[start_index]
            start_index += 1
        
    ls.sort(key=lambda x : (x[1] - x[0], x[0]))
    
    return list(ls[0])
            