import sys
input = sys.stdin.readline

ls = [int(input()) for i in range(9)]
re = []
sumv = sum(ls)
for i in range(9):
    if len(re) == 2:
        break
    for j in range(9):
        if i == j:
            continue
        if sumv - ls[i] - ls[j] == 100:
            re.append(ls[i])
            re.append(ls[j])
            break
            
ls = [i for i in ls if i not in re]
ls.sort()
for i in ls:
    print(i)
    

