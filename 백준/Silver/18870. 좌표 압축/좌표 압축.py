import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().strip().split()))
se = set(li)
_li = list(se)
_li.sort()

dic = {}
for i in range(len(_li)):
    dic[_li[i]] = i
__li = [str(dic[i]) for i in li]
print(" ".join(__li))
