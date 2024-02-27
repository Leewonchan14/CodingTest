a_int = ord("A")
z_int = ord("Z")


def solution(name):
    count = 0
    index = 0
    length = len(name)
    while index < length:
        s = name[index]

        # 위 아래 판단후 더해주기
        s_int = ord(s)
        down_count = z_int - s_int + 1
        up_count = s_int - a_int

        count += min(down_count, up_count)

        # 다음 index 정하기
        temp_index = index + 1
        # 마지막이 아니고 다음이 A 라면
        while temp_index < length and name[temp_index] == "A":
            temp_index += 1

        # 마지막까지 A라면
        if temp_index == length:
            break

        # 오른쪽으로 A가 안나올때 까지 끝까지 간 count
        right_count = temp_index - index

        # 왼쪽으로 갔을때 count
        left_count = index + length - temp_index

        count += min(left_count, right_count)

        index = temp_index

    return count