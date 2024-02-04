import sys

n = int(input())
count = 1
s = sys.stdin.readline().rstrip()
l = list(map(int, s.split()))
li = []
while True:
    while True:
        if len(l) != 0 and l[0] == count:
            l.pop(0)
            count += 1
            continue

        if len(li) != 0 and li[-1] == count:
            li.pop()
            count += 1
            continue
        break
    if len(l) != 0:
        li.append(l.pop(0))
    else:
        break

if len(li) == 0:
    print("Nice")
else:
    print("Sad")
