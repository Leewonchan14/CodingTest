import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

def move(start, end, other, cnt, ls):
    if cnt == 1:
        ls.append((start, end))
        return
    
    move(start, other, end, cnt - 1, ls)
    move(start, end, other, 1, ls)
    move(other, end, start, cnt - 1, ls)
    
result = []
move(1, 3, 2, n, result)

print(len(result))
for s, e in result:
    print(f"{s} {e}")