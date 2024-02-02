import sys

li = []
while True:
    try:
        s = sys.stdin.readline()
        li.append(int(s) % 42)
    except Exception as e:
        break
print(len(set(li)))