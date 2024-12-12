def recur(n, li):
    if n == 0:
        return li

    if n >= 300:
        li[0] += 1
        li = recur(n - 300, li)

    elif n >= 60:
        li[1] += 1
        li = recur(n - 60, li)

    elif n >= 10:
        li[2] += 1
        li = recur(n - 10, li)

    elif n > 0:
        li.append(-1)

    return li


n = int(input())
key = recur(n, [0, 0, 0])
if key[-1] == -1:
    print(-1)
else:
    print(" ".join([str(i) for i in key]))
