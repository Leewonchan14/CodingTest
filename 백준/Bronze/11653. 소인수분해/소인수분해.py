n = int(input())

count = 2
while n != 1:
    if n % count == 0:
        print(count)
        n = n // count
        continue
    count+=1
    if count**2 > n:
        print(n)
        break

            