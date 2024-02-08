n = int(input())
for i in range(n):
    a, b, = map(int, input().split())
    mul1 = 1
    mul2 = 1
    for j in range(b, b - a, -1):
        mul1 *= j
    for j in range(a, 0, -1):
        mul2 *= j

    print(mul1 // mul2)
