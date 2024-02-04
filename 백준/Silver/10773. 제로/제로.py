import sys

n = int(input())
li = []
for i in range(n):
    s = int(sys.stdin.readline().rstrip())
    if s == 0:
        li.pop()
    else:
        li.append(s)
print(sum(li))
