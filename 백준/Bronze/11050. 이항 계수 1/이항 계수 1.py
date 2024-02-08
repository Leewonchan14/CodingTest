a, b, = map(int, input().split())
mul1 = 1
mul2 = 1
for i in range(a, a - b, -1):
    mul1 *= i
for i in range(1, b + 1):
    mul2 *= i
print(mul1 // mul2)

    
