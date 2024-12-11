from collections import deque


def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))
    shoot = []
    
    for s,e in targets:
        if shoot and s < shoot[-1] < e:
            continue
            
        shoot.append(e - 0.5)
    
    return len(shoot)



