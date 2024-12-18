def combi(n, k):
    li = []
    result = []
    
    def recur():
        if len(li) == k:
            result.append(li[:])
            return
        
        for i in range(n):
            if not li or i > li[-1]:
                li.append(i)
                recur()
                li.pop()
    
    recur()
    return result

def main(n, maps):
    minv = float('inf')
    combiNto2 = combi(n // 2, 2)
    for teamA in combi(n, n // 2):
        teamB = [i for i in range(n) if i not in teamA]
        sumA = sum([maps[teamA[a]][teamA[b]] + maps[teamA[b]][teamA[a]] for a,b in combiNto2])
        sumB = sum([maps[teamB[a]][teamB[b]] + maps[teamB[b]][teamB[a]] for a,b in combiNto2])
        
        minv = min(minv, abs(sumA - sumB))
        
    return minv
    

import sys

input = sys.stdin.readline

n = int(input())
maps = [[int(i) for i in input().split()] for _ in range(n)]

print(main(n, maps))