li = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

for i in range(n):
    a ,b = map(int, input().split())
    for j in range( b - 1, b + 9):
        for k in range(a-1,a+9):
            if li[j][k] == 0 :
                li[j][k] += 1
_sum = 0
for i in li:
    _sum += sum(i)

print(_sum)