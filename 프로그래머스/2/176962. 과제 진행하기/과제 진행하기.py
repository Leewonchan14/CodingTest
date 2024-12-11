from collections import deque


def toTime(s):
    h, m = map(int, s.split(":"))
    return h * 60 + m


def solution(plans):
    plans.sort(key=lambda x: toTime(x[1]))
    result = []
    plans = deque(plans)
    title, t, gap = plans.popleft()
    stop = [(title, int(gap))]
    time = 0
    pretime = toTime(t)
    for title, t, gap in plans:
        gap = int(gap)
        time = toTime(t)

        flow = time - pretime

        while stop and flow > 0:
            sT, sGap = stop.pop()
            if sGap > flow:
                stop.append((sT, sGap - flow))
                break
            else:  # flow >= sGap
                flow -= sGap
                result.append(sT)

        stop.append((title, gap))
        pretime = time

    while stop:
        result.append(stop.pop()[0])

    return result


# solution(
#     [
#         ["science", "12:40", "50"],
#         ["music", "12:20", "40"],
#         ["history", "14:00", "30"],
#         ["computer", "12:30", "100"],
#     ]
# )
