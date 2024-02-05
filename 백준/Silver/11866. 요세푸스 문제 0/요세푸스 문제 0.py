from collections import deque

n, k = map(int, input().split())
li = list(range(1, n + 1))
que = deque(li)

answer = []

count = 1
while len(que) != 0:
    if count == k:
        answer.append(str(que.popleft()))
        count = 1
        continue

    que.append(que.popleft())
    count += 1

print("<" + ", ".join(answer) + ">")
