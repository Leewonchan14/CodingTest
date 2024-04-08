from collections import deque

rs = []


def dfs(linked, start, ls, count):
    if len(ls) == count + 1:
        rs.append(ls[:])
        return

    for i in range(len(linked[start])):
        if not linked[start][i][1]:
            linked[start][i][1] = True
            ls.append(linked[start][i][0])
            dfs(linked, linked[start][i][0], ls, count)
            linked[start][i][1] = False
            ls.pop()


def solution(tickets):
    linked = {}
    count = 0
    for a, b in tickets:
        linked[a] = linked.get(a, [])
        linked[a].append([b, False])
        count += 1

        linked[b] = linked.get(b, [])

    dfs(linked, "ICN", ["ICN"], count)

    rs.sort(key=lambda x: "".join(x))

    return rs[0]
