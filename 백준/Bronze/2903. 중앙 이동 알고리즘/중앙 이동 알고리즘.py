def move(n):
    if n == 0:
        return 2
    return (move(n - 1) * 2) - 1

print(move(int(input()))**2)