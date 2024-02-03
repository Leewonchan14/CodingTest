count = 1
now = 666
n = int(input())
while True:
    if n == count:
        break
    now += 1
    if "666" in str(now):
        count += 1
    
print(now)
    
    
    