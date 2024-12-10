li = [1, 1, 2, 4]


def recursive(n):
    if n <= 3:
        return str(li[n])

    post = ""
    if n % 3 == 0:
        n = n // 3 - 1
        post = "4"
    else:
        post = str(li[n % 3])
        n //= 3

    return recursive(n) + post


def solution(n):
    return recursive(n)

