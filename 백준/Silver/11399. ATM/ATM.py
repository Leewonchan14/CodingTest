n = int(input())
li = list(map(int,input().split()))
li.sort()
print(sum([sum(li[:i + 1]) for i in range(n)]))
