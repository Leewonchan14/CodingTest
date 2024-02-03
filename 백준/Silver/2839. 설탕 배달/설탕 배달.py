n = int(input())
f = n // 5
div = n % 5
an = -1
for i in range(f, -1 , -1):
    if div % 3 == 0:
        an = i + div // 3
        break
    div += 5

print(an)