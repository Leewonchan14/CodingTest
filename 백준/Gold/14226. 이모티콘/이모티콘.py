import sys

from collections import deque

input = sys.stdin.readline


def main(n):
    visited = set()
    # weights = [float("inf")] * (10**3 * 3 + 1)
    que = deque()
    visited.add((1, 0))
    # weights[1] = 0
    que.append((1, 0, 0))

    while que:
        k, cnt, t = que.popleft()
        if k == n:
            return cnt

        # 1. -1
        if 0 <= k - 1 and (k - 1, t) not in visited:
            visited.add((k - 1, t))
            que.append((k - 1, cnt + 1, t))

        # 2. paste
        if t > 0 and 0 <= k + t < 1000 * 3 and (k + t, t) not in visited:
            visited.add((k + t, t))
            que.append((k + t, cnt + 1, t))

        # 3. copy
        if (k, k) not in visited:
            visited.add((k, k))
            que.append((k, cnt + 1, k))


n = int(input())
print(main(n))
