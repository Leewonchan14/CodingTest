def solution(s):
    target = ""
    target_count = 0
    other_count = 0
    answer = 0
    for i in s:
        if target == "":
            target = i
            target_count += 1
            continue
        
        if i == target:
            target_count += 1
            
        if target != i:
            other_count += 1
            
        if target_count == other_count:
            answer += 1
            target = ""
            target_count = 0
            other_count = 0
        
    if target != "":
        answer += 1
        
    return answer