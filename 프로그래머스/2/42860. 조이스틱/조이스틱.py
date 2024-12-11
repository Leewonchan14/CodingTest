def updown(target):
    if ord(target) <= (ord("A") + ord("Z")) // 2:
        return ord(target) - ord("A")

    return ord("Z") - ord(target) + 1


def leftright(name):
    minv = len(name) - 1

    for x in range(len(name) - 1):
        y = x + 1
        while y < len(name) and name[y] == "A":
            y += 1

        # left + right
        y = len(name) - y
        a = y + y + x
        # right + left + left
        b = x + x + y
        minv = min(minv, a, b)

    return minv


def solution(name):
    name = list(name)
    cnt = 0
    for n in name:
        cnt += updown(n)

    cnt += leftright(name)

    return cnt
