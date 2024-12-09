import math


def allNumbers(numbers, li, visited, l, result):
    if len(li) == l:
        result.append(li[:])
        return

    for i, n in enumerate(numbers):
        if visited[i]:
            continue

        li.append(n)
        visited[i] = True
        allNumbers(numbers, li, visited, l, result)
        visited[i] = False
        li.pop()


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    nums = set()
    for i in range(1, len(numbers) + 1):
        visited = [False for i in numbers]
        result = []
        allNumbers(numbers, [], visited, i, result)
        nums.update(set([int("".join(n)) for n in result]))

    return len([x for x in nums if isPrime(x)])
