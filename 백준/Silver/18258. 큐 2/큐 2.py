# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
from collections import deque
que = deque()
n = int(input())
for i in range(n):
    s = sys.stdin.readline().rstrip().split()
    if len(s) > 1:
        que.append(s[1])
        continue

    s = s[0]
    if s == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
        continue

    if s == "size":
        print(len(que))
        continue

    if s == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
        continue

    if s == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
        continue
    if s == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
        continue

