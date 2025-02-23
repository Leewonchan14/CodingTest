import sys

input = sys.stdin.readline

n = int(input())

def main():
    def recur(n):
        if n == 0:
            return 1
        return recur(n - 1) * n
    
    print(recur(n))

main()