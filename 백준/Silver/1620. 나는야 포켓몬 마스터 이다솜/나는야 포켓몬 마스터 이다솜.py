import sys
a,b = map(int, input().split())
dic = {}
for i in range(a):
    s = sys.stdin.readline().rstrip()
    dic[s] = i + 1
    dic[i + 1] = s

for i in range(b):
    s = sys.stdin.readline().rstrip()
    key = s
    try:
        key = int(s)
    except Exception as e:
        pass
    print(dic[key])
        
    