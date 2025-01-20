import sys
from collections import deque

input = sys.stdin.readline

a, b, c = map(int, input().split())
visited = set()
visited.add(",".join(map(str, sorted([a, b, c]))))


def find_group(tu):
    result = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            if tu[i] < tu[j]:
                result.append((i, j))

    return result


def main():
    que = deque()
    que.append([a, b, c])

    while que:
        tu = que.popleft()
        if tu[0] == tu[1] == tu[2]:
            return 1

        for i, j in find_group(tu):
            k = 3 - i - j
            li = [0, 0, 0]

            li[i] = tu[i] * 2
            li[j] = tu[j] - tu[i]
            li[k] = tu[k]

            str_li = ",".join(map(str, sorted(li)))

            if str_li not in visited:
                visited.add(str_li)
                que.append(li)

    return 0


print(main())
