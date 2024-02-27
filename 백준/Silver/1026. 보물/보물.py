from sys import stdin

length = int(input())
# length = 5

# a = list(map(int, "1 1 1 6 0".split()))
# b = list(map(int, "2 7 8 3 1".split()))
a = list(map(int, stdin.readline().rstrip().split()))
b = list(map(int, stdin.readline().rstrip().split()))

a.sort()
b.sort(reverse=True)

print(sum(map(lambda x: x[0] * x[1], zip(a, b))))
