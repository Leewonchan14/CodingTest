a,b,c = map(int, input().split())

s= ((c - a) + (a - b - 1)) // (a - b)
print(s+1)