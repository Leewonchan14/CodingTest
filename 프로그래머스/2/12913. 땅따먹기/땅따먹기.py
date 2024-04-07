def solution(land):
    for row in range(1, len(land)):
        for i in range(4):
            land[row][i] += max([land[row - 1][j] for j in range(4) if j != i])
    return max(land[-1])
    
            
            