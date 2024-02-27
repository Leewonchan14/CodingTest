n = int(input())
n = 1000 - n
# n = 1000 -380

li = list(map(int, "500 100 50 10 5 1".split()))


count = 0

for i in li:
    div = n // i
    count += div
    n = n % i

print(count)
