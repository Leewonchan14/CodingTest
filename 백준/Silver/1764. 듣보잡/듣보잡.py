a,b = map(int, input().split())
_a = set()
_b = set()
for i in range(a):
    _a.add(input())
for i in range(b):
    _b.add(input())
li = list(_a&_b)
li.sort()
print(len(li))
for i in li:
    print(i)