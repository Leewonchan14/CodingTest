li = []
for i in range(int(input())):
    a, b = input().split()
    li.append([a,b,i])

li.sort(key=lambda v : (int(v[0]), v[2]))
for i in li:
    print(f"{i[0]} {i[1]}")