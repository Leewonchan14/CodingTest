import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    arr.append(a + b)
    
print(*arr, sep="\n")