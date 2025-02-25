import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(i) for i in input().split()]
arr.sort()


def main():
    li = []

    def recur():
        if len(li) == m:
            print(*[arr[i] for i in li])
            return

        prev = -1
        for i in range(n):
            if (not li or i > li[-1]) and prev != arr[i]:
                prev = arr[i]
                li.append(i)
                recur()
                li.pop()

    recur()


main()
