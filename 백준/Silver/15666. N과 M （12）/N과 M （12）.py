import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(i) for i in input().split()]
arr = list(set(arr))
arr.sort()


def main():
    li = []

    def recur():
        if len(li) == m:
            print(*[arr[i] for i in li])
            return

        for i in range(len(arr)):
            if not li or i >= li[-1]:
                li.append(i)
                recur()
                li.pop()

    recur()


main()
