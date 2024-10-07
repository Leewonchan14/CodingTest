n, m = map(int, input().split())

arr = list(map(str, range(1, n + 1)))

def recursive(li, k):
    if k == m:
        print(" ".join(li))
        return

    for i in arr:
        if not li or li[-1] < i:
            li.append(i)
            recursive(li, k + 1)
            li.pop()


recursive([], 0)