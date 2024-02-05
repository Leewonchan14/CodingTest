a, b, = map(int, input().split())

l1 = [list(map(int, input().split())) for _ in range(a)]

l2 = [list(map(int, input().split())) for _ in range(a)]

for e in [[str(l1[i][j] + l2[i][j]) for j in range(len(l1[0]))] for i in range(len(l1))]:
    print(" ".join(e))