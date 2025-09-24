import sys
import math


input = sys.stdin.readline


def main():
    c = int(input())

    for _ in range(c):
        li = [int(i) for i in input().split()[1:]]
        avg = sum(li) / len(li)
        cnt = len([i for i in li if i > avg])
        print(str(round((cnt / len(li)) * 100, 3)).ljust(2, "0") + "%")


main()
