key = "A+ A0 B+ B0 C+ C0 D+ D0 F".split()
value = "4.5 4.0 3.5 3.0 2.5 2.0 1.5 1.0 0.0".split()
value = list(map(float, value))
dic = dict(zip(key, value))

li = []

_sum = 0

for i in range(20):
    _ , score, _score = input().split()
    if _score == "P":
        continue
    li.append(float(score) * dic[_score])
    _sum += float(score)
    
if _sum == 0:
    print(0)
else:
    print(sum(li)/_sum)
    