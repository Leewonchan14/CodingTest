import sys

sys.setrecursionlimit(10 ** 9)

from collections import deque

muliC = "C,C#,D,D#,E,F,F#,G,G#,A,A#,B"
muliC = muliC.split(",")


def toTime(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def timeGap(a, b):
    return abs(toTime(a) - toTime(b))


def toMusicList(m, li):
    m = list(m)
    while m:
        s = m.pop()
        if s == "#":
            s = m.pop().lower()
        li.appendleft(s)
        
    return li


def toStartEndGapTitleMuli(m):
    a, b, c, d = m.split(",")
    return toTime(a), timeGap(a, b), c, toMusicList(d, deque())


def solution(m, musicinfos):
    m = "".join(toMusicList(m, deque()))
    result = []
    for i in musicinfos:
        start, gap, title, muli = toStartEndGapTitleMuli(i)
        
        if m in ("".join(muli) * gap)[:gap]:
            result.append((-gap, start, title))

    result.sort()

    if not result:
        return "(None)"

    return result[0][2]


# solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
