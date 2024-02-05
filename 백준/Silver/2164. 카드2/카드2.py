from collections import deque

# 카드는 제일 위에서부터 1234 의 순서로 놓여있다.
# 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다.
# 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다.
# 마지막으로 2를 버리고 나면,
# 남는 카드는 4가 된다.
n = int(input())
li = list(range(n, 0, - 1))
que = deque(li)
while True:
    if len(que) == 1:
        break

    que.pop()

    if len(que) == 1:
        break

    que.insert(0, que.pop())

print(que[0])
