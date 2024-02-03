a = []
b = []
for i in range(3):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)
a.sort()
b.sort()

print(f"{sum(a) - a[1] * 2} {sum(b) - 2*b[1]}")