
def solution(sides):
    cot = 0
    for i in range(1, sum(sides)):
        sides.append(i)
        m = max(sides)
        if sum(sides) - m > m:
            cot += 1
        
        sides.remove(i)
    return cot