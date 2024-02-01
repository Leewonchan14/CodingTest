def solution(s1, s2):    
    count = 0
    
    for i in s1:
        count += s2.count(i)
        
    return count
