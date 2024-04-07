from collections import deque


def solution(s):
    rs = []
    for i in range(1, len(s)):
        spl = []
        for j in range(0, len(s), i):
            spl.append(s[j:j + i])

        count = 0
        index = 0

        ls = []
        temp = spl[index]
        while True:
            if index < len(spl) and temp == spl[index]:
                count += 1
                index += 1
                continue

            ls.append((str(count) if count != 1 else "") + temp)
            count = 0

            if index >= len(spl):
                break

            temp = spl[index]

        rs.append(len("".join(ls)))

    rs.sort()
    return rs[0] if rs else len(s)

