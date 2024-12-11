def recursive(cards, start, visited, li):
    visited[start] = True
    li.append(start)
    ns = cards[start] - 1

    if visited[ns]:
        return li

    return recursive(cards, ns, visited, li)


def solution(cards):
    visited = [False] * len(cards)
    result = []
    for i in range(len(cards)):
        if visited[i]:
            continue
        result.append(len(recursive(cards, i, visited, [])))

    result.sort(reverse=True)

    if len(result) >= 2:
        a, b = result[:2]
        return a * b
    else:
        return 0


