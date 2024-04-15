def isCan(stones, k, n):
    n = n - 1
    cnt = 0
    index = 0
    for s in stones:
        if s - n > 0:
            cnt = 0
            continue
        cnt += 1
        if cnt >= k:
            return False
        
    return True


def solution(stones, k):
    left = 0
    right = max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if isCan(stones, k, mid):
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

    return answer
