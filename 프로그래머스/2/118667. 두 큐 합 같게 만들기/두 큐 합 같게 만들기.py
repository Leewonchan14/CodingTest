from collections import deque

def solution(queue1, queue2):
    a_que = deque(queue1)
    b_que = deque(queue2)
    
    a_sum = sum(queue1)
    b_sum = sum(queue2)
    limit = len(queue1) + len(queue2)
    
    sumv = a_sum + b_sum
    
    if sumv % 2 == 1:
        return -1
    
    count = 0
    
    move = []
    
    while a_sum != b_sum:
        if a_sum > b_sum and b_que:
            pop_item = a_que.popleft()
            a_sum -= pop_item
            
            b_que.append(pop_item)
            b_sum += pop_item
            move.append(1)
            
        elif a_sum < b_sum and a_que:
            pop_item = b_que.popleft()
            b_sum -= pop_item
            
            a_que.append(pop_item)
            a_sum += pop_item
            move.append(-1)
            
        if not a_que or not b_que:
            return -1
        
        if len(move) > limit + 5:
            check = move[-4:]
            if all([check[i] != check[i+1] for i in range(3)]):
                return -1
            
            
        count += 1
            
    return count