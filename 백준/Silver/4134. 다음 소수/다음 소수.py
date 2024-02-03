cache = {0: False, 1: False, 2: True}


def is_prime(_n):
    if _n < 1:
        return False

    if _n in cache:
        return cache[_n]

    index = 2
    while True:
        if _n % index == 0:
            cache[_n] = False
            return cache[_n]
        index += 1
        if index ** 2 > _n:
            cache[_n] = True
            return cache[_n]


n = int(input())
for i in range(n):
    a = int(input())
    if is_prime(a):
        print(a)
    else:
        while True:
            a += 1
            if is_prime(a):
                print(a)
                break
