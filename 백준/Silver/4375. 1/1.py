import sys

input = sys.stdin.readline

while s := input():
    s = int(s)

    i = 1
    while i % s != 0:
        i = i * 10 + 1
    print(len(str(i)))
