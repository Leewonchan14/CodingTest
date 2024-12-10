def isPair(a, b):
    if a == b:
        return True

    # 3, 4
    if min(a, b) * 4 == max(a, b) * 3:
        return True

    # 2, 4
    if min(a, b) * 2 == max(a, b):
        return True

    # 2, 3
    if min(a, b) * 3 == max(a, b) * 2:
        return True

    return False


def recursive(n, li, result):
    if len(li) == 2:
        result.append(li[:])
        return

    for i in range(n):
        if not li or li[-1] > i:
            li.append(i)
            recursive(n, li, result)
            li.pop()


def solution(weights):
    count = {}
    for i in weights:
        count[i] = count.get(i, 0) + 1

    print(count)

    keys = list(count.keys())

    cnt = 0
    for i in range(len(keys)):
        for j in range(i, len(keys)):
            if i == j:
                cnt += (count[keys[i]] ** 2 - count[keys[i]]) // 2

            elif isPair(keys[i], keys[j]):
                cnt += count[keys[i]] * count[keys[j]]

    return cnt


