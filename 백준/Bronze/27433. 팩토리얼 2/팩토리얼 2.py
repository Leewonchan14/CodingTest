import sys

input = sys.stdin.readline

n = int(input())

def main():
    mulv = 1
    for i in range(1, n + 1):
        mulv *= i
    print(mulv)

main()