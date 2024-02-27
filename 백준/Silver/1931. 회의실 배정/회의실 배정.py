from sys import stdin

n = int(input())
li = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

li.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0
for v in li:
    start = v[0]
    now_end = v[1]

    if start < end:
        continue

    count += 1
    end = now_end

print(count)