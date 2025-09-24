bit = [False] * 10000

def d(n):
    return n + sum(int(i) for i in str(n))

for i in range(1, 10000):
    if d(i) < 10000:
        bit[d(i)] = True

for i in range(1, 10000):
    if not bit[i]:
        print(i)