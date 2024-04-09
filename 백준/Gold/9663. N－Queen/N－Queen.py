def solution(n):
    cnt = [0]
    column = set()
    digit_x = set()
    digit_y = set()

    def track(num):
        if num == n:
            cnt[0] += 1
            return

        r = num

        for c in range(0, n):
            if c not in column and r - c not in digit_x and r + c not in digit_y:
                column.add(c)
                digit_x.add(r - c)
                digit_y.add(r + c)
                track(num + 1)
                column.remove(c)
                digit_x.remove(r - c)
                digit_y.remove(r + c)

    track(0)

    return cnt[0]


n = int(input())
print(solution(n))


