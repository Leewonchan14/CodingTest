def allCombi(relation, k, li, result):
    if len(li) == k:
        result.append(set(li[:]))
        return result

    for i in range(len(relation[0])):
        if not li or i > li[-1]:
            li.append(i)
            result = allCombi(relation, k, li, result)
            li.pop()

    return result


def isKey(com, relation):
    com = list(com)
    s1 = set([(*[r[c] for c in com],) for r in relation])
    return len(s1) == len(relation)


def isGoodCombi(com, keys):
    for k in keys:
        if all([k1 in com for k1 in k]):
            return False

    return True


def solution(relation):
    keys = set()
    for i in range(1, len(relation[0]) + 1):
        combi = allCombi(relation, i, [], [])
        for c in combi:
            if isGoodCombi(c, keys) and isKey(c, relation):
                keys.add(tuple(c))

    return len(keys)


# solution(
#     [
#         ["100", "ryan", "music", "2"],
#         ["200", "apeach", "math", "2"],
#         ["300", "tube", "computer", "3"],
#         ["400", "con", "computer", "4"],
#         ["500", "muzi", "music", "3"],
#         ["600", "apeach", "music", "2"],
#     ]
# )
