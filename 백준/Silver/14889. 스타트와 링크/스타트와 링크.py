import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

result = []


def recursive(team_a, n, point):
    if len(team_a) == n // 2:
        team_b = [i for i in range(n) if i not in team_a]

        sumv = 0
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                sumv += data[team_b[i]][team_b[j]]
                sumv += data[team_b[j]][team_b[i]]

        result.append((point, sumv))
        return

    for i in range(n):
        if not team_a or i > team_a[-1]:
            team_a.append(i)
            recursive(team_a, n, sum([data[i][j] for j in team_a]) + sum([data[j][i] for j in team_a]) + point)
            team_a.pop()


recursive([], n, 0)

result.sort(key=lambda x: abs(x[0] - x[1]))

print(abs(result[0][0] - result[0][1]))
