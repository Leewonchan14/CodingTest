def lcm(a, b):
    aa = a
    bb = b
    while a != b:
        if aa < bb:
            aa += a
        else:
            bb += b
    return aa

def gcd(a, b):
    n = min(a, b)
    while a % n != 0 or b % n != 0:
        n -= 1
    return n


a,b = map(int, input().split())
d = gcd(a, b)
print(d)
print(a * b // d)