import sys

li = list(range(1,31))

while True:
    try:
        s = sys.stdin.readline()
        s = int(s)
        li.remove(s)
    except Exception as e:
        break    

li.sort()
print(li[0])
print(li[1])