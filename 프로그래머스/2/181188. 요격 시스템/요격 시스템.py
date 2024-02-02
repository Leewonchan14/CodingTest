def solution(targets):
    shot = 0
    count = 0
    targets = sorted(targets, key=lambda v : (v[1], v[0]))
    
    for start, end in targets:
        if start < shot < end :
            continue
        
        shot = end - 0.5
        print(shot)
        count += 1
    return count