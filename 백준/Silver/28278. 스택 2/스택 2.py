import sys

n = int(input())
li = []
for i in range(n):
    s = sys.stdin.readline().rstrip()
    if s[0] == "1":
        a, b = map(int, s.split())
        li.append(b)
    elif s[0] == "2":
        if len(li) != 0:
            print(li.pop())
        else:
            print(-1)
    elif s[0] == "3":
        print(len(li))
    elif s[0] == "4":
        if len(li) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "5":
        if len(li) != 0:
            print(li[-1])
        else:
            print(-1)
