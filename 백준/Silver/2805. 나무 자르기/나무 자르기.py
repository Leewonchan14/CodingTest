import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
maxv = max(arr)


def search(left, right):
    if left > right:
        return right

    mid = (left + right) // 2

    sumv = sum([max(0, i - mid) for i in arr])

    if sumv < m:
        right = mid - 1
    elif sumv >= m:
        left = mid + 1

    return search(left, right)


def main():
    return search(0, maxv)


print(main())
