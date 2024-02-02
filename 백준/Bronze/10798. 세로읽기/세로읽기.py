li = []
for i in range(5):
    s = input()
    s = s + " " * (15 - len(s))
    li.append(s)

li2 = []
for i in range(15):
    for j in range(5):
        if li[j][i] != " ":
            li2.append(li[j][i])

print("".join(li2))
    