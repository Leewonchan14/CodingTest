n = int(input())
danced = {"ChongChong":0}
count = 0
for i in range(n):
    a, b, = input().split()
    if a in danced or b in danced:
        danced[a] = 0
        danced[b] = 0

print(len(danced.keys()))