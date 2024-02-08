import sys

n = int(input())
count = {}
li = []
sum_ = 0
max_ = 0
for i in range(n):
    now = int(sys.stdin.readline().rstrip())
    sum_ += now
    count[now] = count.get(now, 0) + 1

    li.append(now)

li.sort(key=lambda a: a / 2)

items = list(count.items())

items.sort(key=lambda k: (k[1], k[0]))

max_count = items[-1][1]


def getMax():
    max_ = items[-1][0]
    if len(items) >= 2 and items[-1][1] == items[-2][1]:
        for i in range(len(items) - 1, -1, -1):
            if max_count != items[i][1]:
                return items[i + 2][0]

        if max_ == items[-1][0]:
            return items[1][0]
    return max_


max_ = getMax()

print(int(round(sum_ / n, 0)))
print(li[len(li) // 2])
print(max_)
print(li[-1] - li[0])
