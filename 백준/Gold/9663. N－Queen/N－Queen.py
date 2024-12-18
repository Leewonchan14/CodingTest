def main(n):
    cols = [False] * n
    # +
    rup = [False] * (n * 2)
    # -
    rdown = [False] * (n * 2)

    li = []
    cnt = 0

    def recur(r):
        nonlocal cnt
        if len(li) == n:
            cnt += 1
            return

        for c in range(n):
            if cols[c]:
                continue

            if rup[r + c]:
                continue

            if rdown[r - c + n]:
                continue

            cols[c] = True
            rup[r + c] = True
            rdown[r - c + n] = True
            li.append((r, c))
            recur(r + 1)
            li.pop()
            cols[c] = False
            rup[r + c] = False
            rdown[r - c + n] = False

    recur(0)
    return cnt


n = int(input())
print(main(n))
