def left_right(arr):
    return [r[::-1] for r in arr]


def up_down(arr):
    return arr[::-1]


def spin_right(arr):
    new_arr = [[0] * len(arr) for _ in range(len(arr[0]))]
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            new_arr[c][len(arr) - 1 - r] = arr[r][c]

    return new_arr


def spin_left(arr):
    new_arr = [[0] * len(arr) for _ in range(len(arr[0]))]
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            new_arr[len(arr[0]) - 1 - c][r] = arr[r][c]

    return new_arr


def to_squre(arr):
    row_mid = len(arr) // 2
    col_mid = len(arr[0]) // 2
    new_arr = [
        [[r[:col_mid] for r in arr[:row_mid]], [r[col_mid:] for r in arr[:row_mid]]],
        [[r[:col_mid] for r in arr[row_mid:]], [r[col_mid:] for r in arr[row_mid:]]],
    ]

    return new_arr


def to_flat(squre):
    new_arr = []
    for front, back in squre:
        for i in range(len(front)):
            new_arr.append([*front[i], *back[i]])

    return new_arr


def squre_spin_right(arr):
    new_arr = spin_right(to_squre(arr))

    return to_flat(new_arr)


def squre_spin_left(arr):
    new_arr = spin_left(to_squre(arr))

    return to_flat(new_arr)


def main(arr, calcs):
    for c in calcs:
        if c == 1:
            arr = up_down(arr)
        elif c == 2:
            arr = left_right(arr)

        elif c == 3:
            arr = spin_right(arr)

        elif c == 4:
            arr = spin_left(arr)

        elif c == 5:
            arr = squre_spin_right(arr)

        elif c == 6:
            arr = squre_spin_left(arr)

    for r in arr:
        print(" ".join([str(c) for c in r]))


import sys

input = sys.stdin.readline

n, k, r = map(int, input().split())
arr = [[int(i) for i in input().split()] for _ in range(n)]
calcs = [int(i) for i in input().split()]
main(arr, calcs)
