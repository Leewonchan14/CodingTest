import math
def solution(r1, r2):
    count = 0
    
    r1_sq = r1**2
    r2_sq = r2**2
    
    for x in range(1 , r2):
        max_y = int((r2_sq - x*x)**.5)

        min_y = 0
        if x < r1:
            min_y = int((r1_sq-x*x)**.5)
            if (min_y)**2 + x**2 == r1_sq:
                min_y -=1
        
        count += max_y - min_y
        
    return (count + r2 - r1 + 1) * 4

# print(solution(2,5))
# print(solution(1,5))
# print(solution(100000,1000000))