def isGood(r, c, li1, li2):
    # 모든 r + c 값이 같지 않아야함
    # 모든 r - c 값이 같지 않아야함
    # 모든 r,c 값이 같지 않아야함
    if (r + c) in li1 or (r - c) in li2:
        return False

    return True


result = [0]


def recursive(n, row, li1, li2, columns, cnt):
    if row == n:
        result[0] += 1
        return

    for col in range(n):
        if col in columns:
            continue
        if isGood(row, col, li1, li2):
            columns.add(col)
            li1.add(row + col)
            li2.add(row - col)

            recursive(n, row + 1, li1, li2, columns, cnt)
            columns.remove(col)
            li1.remove(row + col)
            li2.remove(row - col)


def solution(n):
    recursive(n, 0, set(), set(), set(), 0)
    return result[0]


