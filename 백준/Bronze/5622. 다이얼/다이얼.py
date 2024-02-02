key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
value = "22233344455566677778889999"
value = list(map(int, list(value)))
dic = dict(zip(list(key), value))

s = input()

li = [dic[s[i]] for i in range(len(s))]
print(sum(li) + len(li))