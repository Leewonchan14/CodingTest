keys = [int(input()) for i in range(9)]

flag = False
a,b = None, None
for i in range(9):
    if flag:
        break
    for j in range(i + 1, 9):
        if sum(keys) - keys[i] - keys[j] == 100:
            flag = True
            a,b = i,j
            break

keys = [v for i,v in enumerate(keys) if i != a and i != b]
keys.sort()
for i in keys:
    print(i)