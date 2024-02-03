dic = {}
for i in range(int(input())):
    a,b = input().split()
    if b == "enter":
        dic[a] = 0
    else:
        dic.pop(a)
        
keys = list(dic.keys())
keys.sort(reverse=True)
for i in keys:
    print(i)