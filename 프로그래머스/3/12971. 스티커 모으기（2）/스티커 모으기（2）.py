maxv = [-1]
ls = []
length = [0]


def left(v):
    return (length[0] + v - 1) % length[0]


def right(v):
    return (v + 1) % length[0]


def solution(sticker):
    length[0] = len(sticker)
    if length[0] == 1:
        return sticker[0]

    dp0 = sticker[:]
    dp0[1] = dp0[0]
    dp0[-1] = 0
    for i in range(2, length[0]):
        dp0[i] = max(dp0[i - 1], dp0[i - 2] + dp0[i])

    dp1 = sticker[:]

    dp1[0] = 0
    for i in range(2, length[0]):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

    return max(dp0[-1], dp1[-1])


# print(solution(	[14, 6, 5, 11, 3, 9, 2, 10]))
