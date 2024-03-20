def get_time(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])


def solution(book_time):
    rooms = []
    book_time.sort(key=lambda x: (x[0], x[1]))
    now_time = get_time("00:00")
    
    for i in book_time:
        now_time = get_time(i[0])

        # 사람들 내보내기 (모든 room의 끝나는 시간이 현재 시간보다 작은 경우)
        for j in range(len(rooms)):
            if rooms[j] and get_time(rooms[j][1]) <= now_time - 10:
                rooms[j] = False

        # 방 배정하기
        for j in range(len(rooms)):
            if not rooms[j]:
                rooms[j] = i
                break
        else:
            rooms.append(i)

    return len(rooms)
