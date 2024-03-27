def zip(y_gab, x_gab, arr):
    s_y, e_y = y_gab
    s_x, e_x = x_gab
    sumv = sum([sum(i[s_x:e_x]) for i in arr[s_y:e_y]])
    if sumv == 0:
        # 0으로 압축
        return 1, 0
    if sumv == (e_y - s_y) * (e_x - s_x):
        # 1로 압축
        return 0, 1

    # 둘다 아닐때
    mid_y = (s_y + e_y) // 2
    mid_x = (s_x + e_x) // 2
    # 왼쪽 위
    a1, b1 = zip((s_y, mid_y), (s_x, mid_x), arr)
    # 왼쪽 아래
    a2, b2 = zip((mid_y, e_y), (s_x, mid_x), arr)
    # 오른쪽 위
    a3, b3 = zip((s_y, mid_y), (mid_x, e_x), arr)
    # 오른쪽 아래
    a4, b4 = zip((mid_y, e_y), (mid_x, e_x), arr)

    a_ = a1 + a2 + a3 + a4
    b_ = b1 + b2 + b3 + b4
    return a_, b_


def solution(arr):
    return list(zip((0, len(arr)), (0, len(arr)), arr))

