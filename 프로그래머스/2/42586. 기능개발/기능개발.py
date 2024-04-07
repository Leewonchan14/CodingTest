import math
def solution(progresses, speeds):
    index = 0
    ls = []
    days = 0
    while True:
        days += math.ceil((100 - progresses[index]) / speeds[index])
        count = 0
        flag = False
        while progresses[index] + speeds[index] * days >= 100:
            index += 1
            count += 1
            if index >= len(progresses):
                flag = True
                break
            continue
        ls.append(count)
        if flag:
            break
        progresses[index] += speeds[index] * days
    
    return ls
            
        
        
        