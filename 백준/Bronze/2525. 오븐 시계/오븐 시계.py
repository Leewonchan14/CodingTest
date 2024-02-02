# 14 30
# 20

# 14 50

a , b = map(int, input().split())
c = int(input())

a = a + (b + c) // 60
a = a % 24
b = (b + c) % 60
print(f"{a} {b}")
