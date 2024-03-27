def count(n, rel, visited, count_dic):
    visited[n] = True
    if not rel[n]:
        count_dic[n] = 1
        return 1

    sumv = 0
    for re in rel[n]:
        if not visited[re]:
            sumv += count(re, rel, visited, count_dic)

    count_dic[n] = sumv + 1
    return sumv + 1


def solution(n, wires):
    rel = {i + 1: [] for i in range(n)}
    visited = [False] * (n + 1)
    for wire in wires:
        a, b = wire
        rel[a].append(b)
        rel[b].append(a)
    count_dic = {}
    count(1, rel, visited, count_dic)

    count_ls = sorted(count_dic.items(), key=lambda x: abs(2 * x[1] - len(count_dic)))
    return abs(count_ls[0][1] - (len(count_dic) - count_ls[0][1]))


