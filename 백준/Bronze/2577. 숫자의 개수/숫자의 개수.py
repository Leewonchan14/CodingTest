import sys

input = sys.stdin.readline

a, b, c = [int(input()) for _ in range(3)]

dic = {}
for s in str(a * b * c):
    dic[s] = dic.get(s, 0) + 1

for i in range(10):
    print(dic.get(str(i), 0))
