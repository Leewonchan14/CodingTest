import sys
input = sys.stdin.readline

def main():
    n = int(input())
    def recur(n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return recur(n - 1) + recur(n - 2)
    print(recur(n))

main()