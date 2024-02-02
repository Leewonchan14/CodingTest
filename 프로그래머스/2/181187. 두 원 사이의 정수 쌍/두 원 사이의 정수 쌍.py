import math
def solution(r1, r2):
    count = 0
    for x in range(1 , r2):
        max_y = int((r2*r2 - x*x)**.5)
        if (max_y + 1)**2 + x**2 == r2**2:
            max_y +=1

        min_y = 0
        if x < r1:
            min_y = int((r1*r1-x*x)**.5)
            if (min_y)**2 + x**2 == r1**2:
                min_y -=1
        
        count += max_y - min_y
        
    return (count + r2 - r1 + 1) * 4

# print(solution(2,5))
# print(solution(1,5))
# print(solution(100000,1000000))