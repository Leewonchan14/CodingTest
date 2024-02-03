is_prime = [True for _ in range(1000001)]
is_prime[0] = False
is_prime[1] = False
is_prime[2] = True

for i in range(2, 1000001):
    if is_prime[i] == True:
        for j in range(i*2,1000001, i):
            is_prime[j] = False

n = int(input())
for i in range(n):
    s = int(input())
    count = 0
    for j in range(3, (s//2) + 1 , 2):
        if is_prime[j] and is_prime[s-j]:
            count+=1
    if s == 4:
        print(1)
    else:
        print(count)