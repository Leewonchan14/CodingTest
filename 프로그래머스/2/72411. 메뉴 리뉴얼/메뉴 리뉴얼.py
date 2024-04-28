import itertools


def include(a, b):
    return all([s in b for s in list(a)])


def solution(orders, course):
    result = []

    for size in course:
        dic = {}
        for o in orders:
            rs = itertools.combinations(sorted(o), size)
            for r in rs:
                key = "".join(r)
                dic[key] = dic.get(key, 0) + 1

        if not dic:
            continue

        items = dic.items()
        maxv = max(dic.values())
        maxv = 2 if maxv < 2 else maxv

        items = [k for k, v in items if v == maxv]
        for it in items:
            result.append(it)

    result.sort()
    return result


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
