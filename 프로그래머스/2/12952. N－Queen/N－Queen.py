def solution(n):
    rows = {}
    columns = {}
    ry = {}
    rd = {}

    ls = []
    cnt = [0]

    def track(num):
        if num == n:
            cnt[0] += 1
            return

        r = num

        for c in range(0, n):
            if c not in columns:
                if r - c not in ry and r + c not in rd:
                    rows[r] = 0
                    columns[c] = 0
                    ry[r - c] = 0
                    rd[r + c] = 0
                    ls.append((r, c))
                    track(num + 1)
                    ls.pop()
                    rows.pop(r)
                    columns.pop(c)
                    ry.pop(r - c)
                    rd.pop(r + c)


    track(0)

    return cnt[0]
