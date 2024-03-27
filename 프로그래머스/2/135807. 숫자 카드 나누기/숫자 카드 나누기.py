import math


def fuc(arrayA, arrayB):
    gcd = arrayA[0]
    for i in arrayA:
        gcd = math.gcd(gcd, i)

    gcd_primes = []

    index = 1
    while index * index <= gcd:
        if gcd % index == 0:
            gcd_primes.append(index)

            if index * index != gcd:
                gcd_primes.append(gcd // index)
        index += 1

    gcd_primes.sort(reverse=True)

    for i in gcd_primes:
        if all([item % i != 0 for item in arrayB]):
            return i

    return 0


def solution(arrayA, arrayB):
    a = fuc(arrayA, arrayB)
    b = fuc(arrayB, arrayA)
    return max(a, b)


# print(solution([14, 35, 119], [18, 30, 102]))
