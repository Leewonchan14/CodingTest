_sum = int(input())
n = int(input())
__sum = 0
for i in range(n):
    a,b = map(int, input().split())
    __sum += a * b
answer = "Yes" if _sum == __sum else "No"
print(answer)