import math


def isPrime(n):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True

    for i in range(2, math.floor(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


tc = int(input())

li = map(int, input().split())
print(len([i for i in li if isPrime(i)]))
