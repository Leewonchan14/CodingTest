n = input()
n = int(n)

for i in range(n):
    a ,b = input().split()
    a = int(a)
    li = [b[j]* a for j in range(len(b))]
    print("".join(li))
    