li = []
for i in range(5):
    li.append(int(input()))

li.sort()

print(sum(li) // len(li))
print(li[2])