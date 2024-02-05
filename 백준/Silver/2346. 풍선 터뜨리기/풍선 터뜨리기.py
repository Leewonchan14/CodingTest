input()
from collections import deque

li = list(map(int, input().split()))

n_li = list(range(1, len(li) + 1))

que = [i for i in li]

li = []
index = 0
while True:
    if len(que) == 0:
        break

    index = index % len(que)
    pop = que.pop(index)
    li_pop = n_li.pop(index)
    li.append(li_pop)
    if pop > 0:
        pop -= 1
    index = index + pop

print(" ".join(list(map(str, li))))
