n = int(input())
li = []
for i in range(n):
    x,y = map(int, input().split())
    li.append((x,y))
li.sort()
for i in li:
    print(f"{i[0]} {i[1]}")