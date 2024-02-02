s = input().upper()
dic = {}
for i in s:
    dic[i] = dic.get(i,0) + 1

li = list(dic.keys())
li.sort(key = lambda v : dic[v])
if len(li) <= 1:
    print(li[0])
elif dic[li[-2]] == dic[li[-1]]:
    print("?")
else:
    print(li[-1])