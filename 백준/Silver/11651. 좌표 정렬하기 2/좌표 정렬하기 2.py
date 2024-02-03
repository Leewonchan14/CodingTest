n = int(input())
li = []
for i in range(n):
    x, y = map(int, input().split())
    li.append((y,x))
li.sort()

for i in li:
    print(f"{i[1]} {i[0]}")