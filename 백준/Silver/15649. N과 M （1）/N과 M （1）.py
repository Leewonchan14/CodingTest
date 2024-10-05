import itertools
n,m = map(int, input().split())
for i in itertools.permutations(map(str, range(1, n + 1)), m):
    print(" ".join(i))
