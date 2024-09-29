n = int(input())
a = map(int, input().split())
n = int(input())
b = map(int, input().split())

dic = {}

for a1 in a:
   dic[a1] = ""

for b1 in b:
    print(1 if b1 in dic else 0)
