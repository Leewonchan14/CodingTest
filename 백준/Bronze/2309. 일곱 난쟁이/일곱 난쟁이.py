import sys
input = sys.stdin.readline

ls = [int(input()) for i in range(9)]
sumv = sum(ls)
re = []
for i in ls:
    if re:
        break
    for j in ls:
        if i == j :
            continue
        if sumv - i - j == 100:
            re.append(i)
            re.append(j)
            break;
            
ls = [i for i in ls if i not in re]

ls.sort()

for i in ls:
    print(i)