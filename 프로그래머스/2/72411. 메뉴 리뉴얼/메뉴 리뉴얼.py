def dfs(o, n, k, ls, rs):
    if n == k:
        nl = [o[i] for i in ls]
        nl.sort()
        rs.append("".join(nl))
        return

    for i in range(len(o)):
        if not ls or ls[-1] < i:
            ls.append(i)
            dfs(o, n + 1, k, ls, rs)
            ls.pop()


def include(a, b):
    return all([s in b for s in list(a)])


def solution(orders, course):
    result = []

    for size in course:
        size_set = set()
        for o in orders:
            rs = []
            dfs(o, 0, size, [], rs)
            for r in rs:
                size_set.add(r)

        dic = {}
        for r in size_set:
            cnt = 0
            for o in orders:
                if include(r, o):
                    cnt += 1
            dic[r] = cnt

        if not dic:
            continue
        # print(dic)
        items = dic.items()
        maxv = max(dic.values())
        maxv = 2 if maxv < 2 else maxv

        items = [k for k, v in items if v == maxv]
        for it in items:
            result.append("".join(sorted(it)))

    result.sort()
    return result
