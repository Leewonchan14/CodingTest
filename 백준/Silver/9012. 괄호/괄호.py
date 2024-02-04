import sys

n = int(input())
for i in range(n):
    s = sys.stdin.readline().rstrip()

    li = []
    for j in s:
        if len(li) == 0:
            li.append(j)
            continue

        if j == ")":
            if li[-1] == "(":
                li.pop()
            else:
                break
        else:
            li.append(j)
    if len(li) != 0:
        print("NO")
    else:
        print("YES")
