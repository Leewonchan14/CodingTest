import math

n, s = map(int, input().split())
print(math.gcd(*map(lambda x: abs(int(x) - s), input().split())))
