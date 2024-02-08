import sys

n = int(input())
saied = {}
count = 0
for i in range(n):
    s = sys.stdin.readline().rstrip()
    if s == "ENTER":
        saied.clear()
        continue

    if s in saied:
        continue
    elif s not in saied:
        count += 1
        saied[s] = 0


print(count)