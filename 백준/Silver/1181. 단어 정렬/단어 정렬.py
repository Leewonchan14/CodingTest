li = []
for i in range(int(input())):
    li.append(input())

li = list(set(li))
li.sort(key=lambda v : (len(v), v))

for i in li:
    print(i)