import sys
from collections import deque

input = sys.stdin.readline


def main(n, k):
    weights = [float("inf")] * (10**5 + 1)
    que = deque()
    que.append((n, 0))
    weights[n] = 0
    count_dic = {}
    count_dic[n] = count_dic.get(n, 0) + 1
    while que:
        n, cnt = que.popleft()
        count_dic[n] = count_dic.get(n, 0) - 1

        if n == k and count_dic[n] == 0:
            return cnt

        for dn, dc in [(-1, 1), (1, 1), (n, 0)]:
            nn = n + dn
            nc = cnt + dc

            if 0 <= nn < len(weights) and nc < weights[nn]:
                weights[nn] = nc
                count_dic[nn] = count_dic.get(nn, 0) + 1
                que.append((nn, nc))


n, k = map(int, input().split())
print(main(n, k))
