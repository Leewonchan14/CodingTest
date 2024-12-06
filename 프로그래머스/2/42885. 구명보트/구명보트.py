import sys

sys.setrecursionlimit(10 ** 9)

from collections import deque
    
    

def solution(people, limit):
    people.sort()
    people = deque(people)
    k = 0
    while people:
        if len(people) >= 2 and people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()

        else:
            people.pop()
        
        k += 1
        
    return k
