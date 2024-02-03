input()
dic = {}
li = list(map(int, input().split()))
for i in li:
    dic[i] = dic.get(i, 0) + 1

input()

m = list(map(int, input().split()))
print(" ".join([str(dic.get(i, 0)) for i in m]))