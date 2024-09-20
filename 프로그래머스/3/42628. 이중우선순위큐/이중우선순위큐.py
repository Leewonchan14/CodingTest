"""
1. 아이디어
    - 정렬이 되어있는 deque을 이용해 insert, delete 연산을 하며 마지막에 첫원소, 마지막 원소를 반환한다.
    - 원소를 집어넣을때는 이분탐색을 이용한다.

2. 시간 복잡도
    - insert : log(n)
    - 최댓값, 최소값 delete : 1
    1000000 의 경우의 수를 log(n)번
    10 ** 6 == 2 ** 20
    최악의수 => n * log(n)
    => 1000000 * 20 = 2천만 == 가능

3. 자료 구조
    que : Deque
"""

from collections import deque


def index(que, start, end, value):
    if len(que) == 0:
        return 0
    
    mid = (start + end) // 2
    
    if start == end:
        return start
    
    if value <= que[mid]:
        return index(que, start, mid, value)
        
    elif value > que[mid]:
        return index(que, mid + 1, end, value)
    
    
    


def solution(operations):
    que = deque()
    
    # print(dir(que))
    
    for item in operations:
        oper, value = item.split()
        value = int(value)
        
        if oper == "I":
            idx = index(que, 0, len(que), value)
            que.insert(idx, value)
            
        elif oper == "D":
            if que:
                if value == -1:
                    que.popleft()
                elif value == 1:
                    que.pop()
        
    if que:
        return [que[-1], que[0]]
    else:
        return [0, 0]
                

