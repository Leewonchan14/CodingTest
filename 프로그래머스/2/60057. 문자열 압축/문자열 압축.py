from collections import deque


def zip(li):
    que = deque(li)

    result = []

    while que:
        s = que.popleft()
        cnt = 1
        while que and que[0] == s:
            que.popleft()
            cnt += 1

        item = str(cnt if cnt > 1 else "") + s
        result.append(item)

    return len("".join(result))


def split(s, i):
    result = []
    for j in range(0, len(s), i):
        result.append(s[j : j + i])
    return result


def solution(s):
    minv = float("inf")
    for i in range(1, len(s) + 1):
        minv = min(zip(split(s, i)), minv)

    return minv


