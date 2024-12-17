import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


# memozation combination
def combi(n, k):
    li = []
    result = []

    def recur():
        if len(li) == k:
            result.append(li[:])
            return result

        for i in range(n):
            if not li or i > li[-1]:
                li.append(i)
                recur()
                li.pop()

        return result

    return recur()


def sumTeam(arr, n, team):
    li = []

    def recur(sumv):
        if len(li) == 2:
            a, b = li
            return sumv + arr[team[a]][team[b]]

        for i in range(n):
            li.append(i)
            sumv = recur(sumv)
            li.pop()

        return sumv

    return recur(0)


def main(n, arr):
    minv = float("inf")

    for j in range(2, n // 2 + 1):

        twoA = combi(j, 2)
        twoB = combi(n - j, 2)

        for teamA in combi(n, j):
            teamB = [i for i in range(n) if i not in teamA]
            sumA = sum(
                [arr[teamA[a]][teamA[b]] + arr[teamA[b]][teamA[a]] for a, b in twoA]
            )
            sumB = sum(
                [arr[teamB[a]][teamB[b]] + arr[teamB[b]][teamB[a]] for a, b in twoB]
            )
            minv = min(minv, abs(sumA - sumB))

    return minv


n = int(input())
arr = [[int(i) for i in input().split()] for _ in range(n)]

print(main(n, arr))

# print(combi(4, 2))
