def solution(n):
    ls = []
    mapper = ["0","1", "2", "4"]

    while True:
        div = n % 3
        if div == 0:
            n = n // 3 - 1
            ls.append("4")
        else:
            ls.append(mapper[n % 3])
            n = n // 3

        if n == 0:
            break

    ls.reverse()

    return "".join(ls)

