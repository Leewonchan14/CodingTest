a, b, c = map(int, input().split())


def main(a, b, c):
    if b >= c:
        return -1

    return (a // (c - b)) + 1


print(main(a, b, c))
