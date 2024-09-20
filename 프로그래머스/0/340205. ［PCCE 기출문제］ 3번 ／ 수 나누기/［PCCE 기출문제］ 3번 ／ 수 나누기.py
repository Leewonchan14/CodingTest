number = int(input())

answer = 0

for i in map(int, str(number)[::2]):
    answer += number % 100
    number //= 100

print(answer)