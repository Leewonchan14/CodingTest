import math


a,b = map(int, input().split())
c,d = map(int, input().split())

_a = math.gcd(a,b)
a = a // _a
b = b // _a

_b = math.gcd(c,d)
c = c // _b
d = d // _b

_c = math.lcm(b,d)

_d = a * (_c // b) + c * (_c // d)
_e = math.gcd(_c, _d)

print(f"{_d // _e} {_c // _e}")

