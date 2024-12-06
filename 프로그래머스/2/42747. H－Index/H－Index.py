def solution(citations):
    # citations = [10,9,8]
    
    # citations = [9, 7, 6, 2, 1]
    answer = 0
    value = 0
    citations.sort(reverse=True)
    for i,v in enumerate(citations):
        value = max(value, min(i + 1, v))
            
    return value
    