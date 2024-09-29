import sys
input = sys.stdin.readline

stk = []

for _ in range(int(input())):
    s = input().strip()

    ar = s.split(" ")

    if ar[0] == "push":
        stk.append(ar[1])
        continue
    elif ar[0] == "pop":
        print(-1 if not stk else stk.pop())
        continue
    elif ar[0] == "size":
        print(len(stk))
        continue
    elif ar[0] == "empty":
        print(1 if not stk else 0)
        continue
    elif ar[0] == "top":
        print(-1 if not stk else stk[-1])
