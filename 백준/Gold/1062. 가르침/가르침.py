import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
sets = [set(list(a)) for a in arr]


def count_possible(select):
    cnt = 0
    for ss in sets:
        if len(ss - select) == 0:
            cnt += 1

    return cnt


def combi(n, k, callback):
    li = []

    if k > n:
        callback(list(range(n)))
        return

    def recur():
        if len(li) == k:
            callback(li)
            return

        for i in range(n):
            if not li or i > li[-1]:
                li.append(i)
                recur()
                li.pop()

    recur()


def main():
    total = list(set.union(*sets) - set("antic"))
    select = set("antic")
    maxv = 0

    def callback(li):
        nonlocal maxv
        maxv = max(maxv, count_possible(select | set([total[i] for i in li])))

    combi(len(total), k - 5, callback)

    return maxv


print(main())
