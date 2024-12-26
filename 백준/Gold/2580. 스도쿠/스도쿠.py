import sys

input = sys.stdin.readline


def to_square_idx(y, x):
    return (y // 3 * 3) + (x // 3)


square = []
r_not_in = []
c_not_in = []
zeros = []


def get_not_in():
    for i in range(9):
        r = i // 3
        c = i % 3
        not_in = [False for _ in range(9)]
        for rr in maps[r * 3 : r * 3 + 3]:
            for cc in rr[c * 3 : c * 3 + 3]:
                if cc == 0:
                    continue

                not_in[cc - 1] = True
        square.append(not_in)

    for r in maps:
        r_not_in.append([(c in r) for c in range(1, 10)])

    cc = [[maps[r][c] for r in range(9)] for c in range(9)]
    for c in cc:
        c_not_in.append([(i in c) for i in range(1, 10)])


def get_zeros():
    for r in range(9):
        for c in range(9):
            if maps[r][c] == 0:
                zeros.append((r, c))


def write(y, x, v, isTrue):
    maps[y][x] = (v + 1) if isTrue else 0
    square[to_square_idx(y, x)][v] = isTrue
    r_not_in[y][v] = isTrue
    c_not_in[x][v] = isTrue


def get_values(y, x):
    return [
        i
        for i in range(9)
        if not square[to_square_idx(y, x)][i]
        and not r_not_in[y][i]
        and not c_not_in[x][i]
    ]


def main(maps):
    get_zeros()
    get_not_in()

    def recur(cnt):
        if cnt == len(zeros):
            for r in maps:
                print(" ".join([str(i) for i in r]))
            return True

        r, c = zeros[cnt]

        for v in get_values(r, c):
            write(r, c, v, True)
            if recur(cnt + 1):
                return True

            write(r, c, v, False)

    recur(0)


maps = [[int(i) for i in input().split()] for _ in range(9)]
main(maps)
