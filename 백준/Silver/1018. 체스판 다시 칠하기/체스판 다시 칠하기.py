row, col = map(int, input().split())
li_w = [[0 for _ in range(col)] for _ in range(row)]
li_b = [[0 for _ in range(col)] for _ in range(row)]

for i in range(row):
    s = input()
    for j in range(col):
        now = s[j]
        if now == "W":
            # "W"가 시작인 경우 검은색이 바뀌어야 함
            if (i + j) % 2 == 0:
                li_b[i][j] = 1
            else:
                li_w[i][j] = 1

        elif now == "B":
            if (i + j) % 2 == 0:
                li_w[i][j] = 1
            else:
                li_b[i][j] = 1
_min = 64
for i in range(0, row - 7):
    for j in range(0, col - 7):

        w_min = sum([sum(k[j:j + 8]) for k in li_w[i:i + 8]])
        b_min = sum([sum(k[j:j + 8]) for k in li_b[i:i + 8]])
        d = [w_min, b_min]

        if min(d) < _min:
            _min = min(d)

print(_min)
