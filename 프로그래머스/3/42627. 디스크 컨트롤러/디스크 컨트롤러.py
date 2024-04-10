import heapq
from collections import deque


def solution(jobs):
    ls = []
    jobs.sort()
    jobs = deque(jobs)
    time = 0
    sumv = []
    length = len(jobs)

    while jobs or ls:
        while jobs and jobs[0][0] <= time:
            a, b = jobs.popleft()
            heapq.heappush(ls, (b, a))

        if ls:
            delay = 0
            gap, start = heapq.heappop(ls)
            if time >= start:
                delay += time - start

            delay += gap

            sumv.append(delay)
            time += gap
        else:
            time += 1

    print(sumv)

    return sum(sumv) // length

