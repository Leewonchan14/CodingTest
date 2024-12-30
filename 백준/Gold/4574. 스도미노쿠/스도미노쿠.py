maps = []
rows_map = {v: i for i, v in enumerate("ABCDEFGHI")}
visited = set()


def get_rc(po):
    return rows_map[po[0]], int(po[1]) - 1


def get_possible(r, c, d):
    rr, cc = r // 3 * 3, c // 3 * 3
    square = [maps[y][x] for y in range(rr, rr + 3) for x in range(cc, cc + 3)]
    rows = maps[r]
    cols = [maps[i][c] for i in range(9)]

    li = []
    for i in range(1, 10):
        if i not in square and i not in rows and i not in cols:
            li.append(i)

    if d == 0:
        ncc = (c + 1) // 3 * 3
        if ncc != cc:
            cc = ncc
            square = [
                [maps[y][x] for x in range(cc, cc + 3)] for y in range(rr, rr + 3)
            ]

        cols = [maps[i][c + 1] for i in range(9)]
    else:
        nrr = (r + 1) // 3 * 3
        if nrr != rr:
            rr = nrr
            square = [
                [maps[y][x] for x in range(cc, cc + 3)] for y in range(rr, rr + 3)
            ]

        rows = maps[r + 1]

    result = []

    for i in li:
        for j in range(1, 10):
            if (
                i != j
                and j not in square
                and j not in rows
                and j not in cols
                and (i, j) not in visited
                and (j, i) not in visited
            ):
                result.append((i, j))

    return result


def main():
    d = [[0, 1], [1, 0]]

    def recur(cnt):
        if all(all(cell != 0 for cell in row) for row in maps):
            for r in maps:
                print("".join(map(str, r)))
            return True

        for e in range(81):
            r, c = divmod(e, 9)

            if maps[r][c] != 0:
                continue

            possible = [[], []]

            # 가로 가능하면
            if c + 1 < len(maps[0]) and maps[r][c + 1] == 0:
                possible[0] = get_possible(r, c, 0)

            # 세로 가능하면
            if r + 1 < len(maps) and maps[r + 1][c] == 0:
                possible[1] = get_possible(r, c, 1)

            for p in range(2):
                if not possible[p]:
                    continue
                for a, b in possible[p]:
                    visited.add((a, b))
                    visited.add((b, a))
                    nr = r + d[p][0]
                    nc = c + d[p][1]
                    maps[r][c] = a
                    maps[nr][nc] = b
                    if recur(cnt + 1):
                        return True
                    maps[r][c] = 0
                    maps[nr][nc] = 0
                    visited.remove((a, b))
                    visited.remove((b, a))

            return

    recur(0)


idx = 0
while True:
    n = int(input())
    if n == 0:
        break
    maps = [[0] * 9 for _ in range(9)]
    visited.clear()
    for i in range(9):
        visited.add((i, i))

    for i in range(n):
        a, po1, b, po2 = input().split()
        a, b = int(a), int(b)
        for v, po in [[a, po1], [b, po2]]:
            r, c = get_rc(po)
            maps[r][c] = v

        visited.add((a, b))
        visited.add((b, a))

    arr = input().split()
    for i in range(1, 10):
        r, c = get_rc(arr[i - 1])
        maps[r][c] = i

    idx += 1
    print("Puzzle", idx)
    main()
