def solution(people, limit):
    people.sort()
    small_idx = 0
    big_idx = len(people) - 1
    
    count = 0
    
    while True:
        if small_idx > big_idx:
            break
            
        small = people[small_idx]
        big = people[big_idx]
        
        if small + big <= limit:
            small_idx += 1
        
        big_idx -= 1
        count += 1
        
    return count
        
        