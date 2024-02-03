li = []
for i in range(3):
    a = int(input())
    li.append(a)
li.sort()
if sum(li) != 180:
    print("Error")
elif li[0] == li[1] == li[2]:
    print("Equilateral")
elif li[0] != li[1] and li[1] != li[2] and li[2] != li[0]:
    print("Scalene")
else:
    print("Isosceles")