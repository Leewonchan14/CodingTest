pre = 1
count = 1
index = 1
next = 0
n = int(input())
while True:
    next = index + count
    if index <= n < next:
        break
    count += 1
    index = next

row = n - index
col = count - row - 1

if count % 2 == 0:
    print(f"{row + 1}/{col + 1}")
else:
    print(f"{col + 1}/{row + 1}")
