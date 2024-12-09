import sys

sys.setrecursionlimit(10 ** 9)

from collections import deque

def recursive(bridge_length, weight, que, time, bridge, now_bridge_length, now_weight):
    if len(que) == 0 and now_weight == 0:
        return time
    
    if bridge:
        pop = bridge.popleft()
        now_bridge_length -= 1
        now_weight -= pop
    
    # 트럭이 올라탈수 있다면
    if now_bridge_length + 1 <= bridge_length and que and now_weight + que[0] <= weight:
        pop = que.popleft()
        bridge.append(pop)
        now_bridge_length += 1
        now_weight += pop
        
    else:
        bridge.append(0)
        
    return recursive(bridge_length, weight, que, time + 1, bridge, now_bridge_length, now_weight)
    
    

def solution(bridge_length, weight, truck_weights):
    que = deque(truck_weights)
    return recursive(bridge_length, weight, que, 0, deque([0] * bridge_length), 0, 0)