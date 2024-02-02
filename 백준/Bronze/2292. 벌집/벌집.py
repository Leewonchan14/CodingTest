def nextMove(n):
    return n*6 - 6

n = int(input())
count = 0
i_ = 1
while True:
    i_ += nextMove(count + 1)
    count += 1
    if i_ >= n :
        break

    
print(count)