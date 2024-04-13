def solution(n, times):
    mx = n * times[-1]
    mn = 0

    answer = float('inf')

    while mn <= mx:
        mid = (mx + mn) // 2
        can_people = sum([mid // t for t in times])

        if can_people >= n:
            answer = min(answer, mid)
            mx = mid - 1
        else:
            mn = mid + 1

    return answer


