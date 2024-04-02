import math
def solution(progresses, speeds):
    stk = []
    total_days = 0
    index = 0
    while index < len(progresses):
        progresses[index] += speeds[index] * total_days
        if len(stk) > 0 and progresses[index] >= 100:
            stk[-1] += 1
            index += 1
            continue
            
        days = (100 - progresses[index]) / speeds[index]
        days = math.ceil(days)
        total_days += days
        
        stk.append(1)
        
        index += 1
    return stk
        