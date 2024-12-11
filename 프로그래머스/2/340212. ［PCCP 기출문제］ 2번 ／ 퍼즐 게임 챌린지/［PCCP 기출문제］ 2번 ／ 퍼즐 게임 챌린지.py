def isGood(diffs, times, limit, level):
    hang = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            hang += times[i]
            continue
        elif diffs[i] > level:
            t = (times[i] + (times[i - 1] if i != 0 else 0)) * (diffs[i] - level)
            t += times[i]
            hang += t

    return hang <= limit


def recursion(diffs, times, limit, level):
    left = 0
    right = level
    mid = 0
    while left < right:
        mid = (left + right) // 2
        if isGood(diffs, times, limit, mid):
            right = mid
        else:
            left = mid + 1

    return right


def solution(diffs, times, limit):
    v = recursion(diffs, times, limit, max(diffs))
    return v if v != 0 else 1


# print(solution([1, 5, 3], [2, 4, 7], 30))
