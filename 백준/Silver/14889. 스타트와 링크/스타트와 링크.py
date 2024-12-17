import sys

input = sys.stdin.readline


def getMid(n, li, result):
    if len(li) == n // 2:
        result.append(li[:])
        return result

    for i in range(n):
        if not li or i > li[-1]:
            li.append(i)
            result = getMid(n, li, result)
            li.pop()

    return result


def get2(n, li, result):
    if len(li) == 2:
        result.append(li[:])
        return result

    for i in range(n):
        li.append(i)
        result = get2(n, li, result)
        li.pop()

    return result


def main(n, arr):
    minv = float("inf")
    two = get2(n // 2, [], [])
    for teamA in getMid(n, [], []):
        teamB = [i for i in range(n) if i not in teamA]
        sumA = sum([arr[teamA[a]][teamA[b]] for a, b in two])
        sumB = sum([arr[teamB[a]][teamB[b]] for a, b in two])
        minv = min(minv, abs(sumA - sumB))

    return minv


n = int(input())
arr = [[int(i) for i in input().split()] for _ in range(n)]

print(main(n, arr))
