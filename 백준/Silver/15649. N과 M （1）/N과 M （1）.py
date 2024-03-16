import itertools

n, a = map(int, input().split())

for i in itertools.permutations(map(str, range(1, n + 1)), a):
    print(" ".join(i))
