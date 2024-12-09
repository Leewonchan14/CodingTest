def solution(n):
    arr = [[0] * i for i in range(1, n + 1)]
    k = 1
    y = 0
    x = 0
    arr[y][x] = k
    k += 1
    while True:
        some = False

        # down
        while y + 1 < len(arr) and arr[y + 1][x] == 0:
            some = True
            y += 1
            arr[y][x] = k
            k += 1

        # right
        while x + 1 < len(arr[y]) and arr[y][x + 1] == 0:
            some = True
            x += 1
            arr[y][x] = k
            k += 1

        # up
        while y - 1 > 0 and x - 1 > 0 and arr[y - 1][x - 1] == 0:
            some = True
            y -= 1
            x -= 1
            arr[y][x] = k
            k += 1

        if not some:
            break

    li = []
    for i in arr:
        li.extend(i)

    return li