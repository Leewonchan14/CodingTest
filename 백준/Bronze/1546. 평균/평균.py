input()
li = list(map(int, input().split()))
_max = max(li)
print(sum(li) / len(li)/ _max * 100)