from collections import deque

def solution(bridge_length, weight, truck_weights):
    none = deque(truck_weights)
    brige = deque([0] * bridge_length)
    time = 0
    sumv = 0
    while none or sumv != 0:
        time += 1
        if brige:
            sumv -= brige.popleft()
            
        if none and sumv + none[0] <= weight:
            sumv += none[0]
            brige.append(none.popleft())
        else:
            brige.append(0)
        
    return time