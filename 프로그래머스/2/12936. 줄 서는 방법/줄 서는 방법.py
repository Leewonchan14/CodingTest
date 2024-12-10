def fact(n):
    if n <= 1:
        return 1

    return n * fact(n - 1)


def recursive(n, k, c, li):
    f = fact(c - 1)
    arr = [i for i in range(1, n + 1) if i not in li]
    li.append(arr[(k - 1) // f])
    if len(li) == n:
        return li
    return recursive(n, k % f, c - 1, li)


def solution(n, k):
    return recursive(n, k, n, [])


