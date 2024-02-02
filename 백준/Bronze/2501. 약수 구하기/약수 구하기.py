a,b = map(int, input().split())
count = 0
index = 1
while True:
    if a % index == 0:
        count += 1
        if count == b:
            print(index)
            break
    index += 1
    if index > a :
        print(0)
        break