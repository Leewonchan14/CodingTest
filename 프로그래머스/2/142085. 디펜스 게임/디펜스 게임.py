import heapq


def recursion(n, k, enemy, start):
    heap = []
    while True:
        if start >= len(enemy):
            return start

        heapq.heappush(heap, -enemy[start])

        if n - enemy[start] >= 0:
            n -= enemy[start]
            start += 1
            continue

        n -= enemy[start]
        while k > 0 and n < 0 and heap:
            n -= heapq.heappop(heap)
            k -= 1

        if k <= 0 and n < 0:
            return start

        start += 1


def solution(n, k, enemy):
    return recursion(n, k, enemy, 0)


# print(solution(2, 4, [3, 3, 3, 3]))
# solution(7, 3, [4, 2, 4, 5, 3, 3, 1])
