is_prime = [True for i in range(10000000)]
is_prime[0] = False
is_prime[1] = False

for i in range(2, 10000000):
    if is_prime[i]:
        for j in range(i + i, 10000000, i):
            is_prime[j] = False

import itertools


def solution(numbers):
    numbers = list(numbers)
    prime_ls = set()
    for i in range(1, len(numbers) + 1):
        per = list(itertools.permutations(numbers, i))
        per = list(map(lambda x: int("".join(list(x))), per))
        per = list(set(per))

        per = list(filter(lambda x: is_prime[x], per))
        for item in per:
            prime_ls.add(item)

    return len(prime_ls)


print(solution("011"))
