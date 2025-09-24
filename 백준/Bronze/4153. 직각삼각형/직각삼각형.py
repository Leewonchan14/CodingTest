import sys

input = sys.stdin.readline


while True:
    a,b,c = sorted([int(i) for i in input().split()])
    if a + b + c == 0:
        break
    s = "wrong"
    if c ** 2 == a ** 2 + b ** 2:
        s = "right"
    print(s)
    
