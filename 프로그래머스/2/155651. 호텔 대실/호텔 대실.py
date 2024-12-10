from collections import deque


def toTime(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def checkRoom(stk, rest_room, time):
    new_stk = []
    for t in stk:
        if t <= time:
            rest_room += 1
        else:
            new_stk.append(t)

    return new_stk, rest_room

def useRoom(time, rooms, end):
    new_rooms = [t for t in rooms if t > time]
    new_rooms.append(end)
    return new_rooms


def solution(book_time):
    book_time.sort(key=lambda x: (x[0], x[1]))
    time = 0
    rooms = []
    maxr = 0
    for s, e in book_time:
        time = toTime(s)
        rooms = useRoom(time, rooms, toTime(e) + 10)
        maxr = max(maxr, len(rooms))

    return maxr


# solution([["09:10", "10:10"], ["10:20", "12:20"]])
