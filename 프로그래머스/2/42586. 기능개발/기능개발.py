import math

def solution(progresses, speeds):
    answer = []
    i = 0
    while i < len(progresses):
        s = speeds[i]
        p = progresses[i]
        
        
        cnt = 0
        t = math.ceil((100 - p) / s)
        while i < len(progresses) and progresses[i] + speeds[i] * t >= 100:
            cnt += 1
            i += 1
            
        answer.append(cnt)
                
    return answer
        
        