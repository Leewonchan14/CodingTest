a = int(input())
my = set(map(int, input().split()))
b = int(input())
_new = list(map(int, input().split()))

li = [str(int(i in my)) for i in _new]
print(" ".join(li))