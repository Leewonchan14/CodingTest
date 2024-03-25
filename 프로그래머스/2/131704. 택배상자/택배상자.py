from collections import deque

def solution(order):
    boxes = deque(range(1, len(order)+1))
    order = deque(enumerate(order))
    sub_con = []
    
    count = 0
    
    while boxes and order:
        # 컨테이너 순서가 맞다면
        if boxes[0] == order[0][1]:
            count += 1
            boxes.popleft()
            order.popleft()
            continue
            
        # 서브 컨테이너 순서가 맞다면
        if len(sub_con) > 0 and sub_con[-1] == order[0][1]:
            count += 1
            sub_con.pop()
            order.popleft()
            continue
            
        # 순서가 틀리다면
        sub_con.append(boxes.popleft())
        
    while len(sub_con) > 0 and sub_con[-1] == order[0][1]:
        # 서브 컨 다 넣어주기
        count += 1
        sub_con.pop()
        order.popleft()
            
    return count