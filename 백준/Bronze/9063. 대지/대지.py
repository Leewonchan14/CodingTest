n = int(input())
x = []
y = []
if n == 1:
    print(0)
    
else:
    for i in range(n):
        a,b = map(int , input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    print((x[-1] - x[0]) * (y[-1] - y[0]))