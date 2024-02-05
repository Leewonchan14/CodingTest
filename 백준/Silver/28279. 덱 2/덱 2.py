import sys
from collections import deque

# 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
# 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
# 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 5: 덱에 들어있는 정수의 개수를 출력한다.
# 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
# 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
# 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
que = deque()
n = int(input())
for i in range(n):
    s = sys.stdin.readline().rstrip()

    if s[0] == "1":
        que.insert(0, int(s.split()[1]))

    if s[0] == "2":
        que.append(int(s.split()[1]))

    if s[0] == "3":
        if len(que) != 0:
            print(que.popleft())
        else:
            print(-1)

    if s[0] == "4":
        if len(que) != 0:
            print(que.pop())
        else:
            print(-1)

    if s[0] == "5":
        print(len(que))

    if s[0] == "6":
        print(int(len(que) == 0))

    if s[0] == "7":
        if len(que) != 0:
            print(que[0])
        else:
            print(-1)

    if s[0] == "8":
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)