input()
m = list(map(int, input().split()))
input()
n = list(map(int, input().split()))

dic = {}
for i in m:
    dic[i] = dic.get(i, 0) + 1

print(" ".join([str(dic.get(i, 0)) for i in n]))


