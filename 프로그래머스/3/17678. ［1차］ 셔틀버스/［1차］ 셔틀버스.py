"""
줄선 순서로 셔틀에 탄다.
셔틀은 9시부터 n 번 t 분 간격으로 온다 (m명이 탑승가능)

9시에 도착한 사람은 9시 셔틀에 탈수있다.
콘은 같이 줄서기 시작했다면 제일 뒤에 선다.
콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하여라
=> 가장 마지막 셔틀에 마지막 순서로 타면 된다.

== 마지막 셔틀의 출발시간에 도착하면 된다.

"""

def time_to_sec(s):
    h, m = map(int,s.split(":"))
    return h * 60 + m

def sec_to_time(t):
    h = str(t // 60)
    if len(h) == 1:
        h = "0" + h
    
    m = str(t % 60)
    if len(m) == 1:
        m = "0" + m
    return f"{h}:{m}"
    

def solution(n, t, m, timetable):
    
    timetable.sort()
    
    start = time_to_sec("09:00")
    limitTime = (n - 1) * t + start
    timetable = list(map(time_to_sec, timetable))
    timetable = list(filter(lambda x : x <= limitTime, timetable))
    length = len(timetable)
    
    
    
    isEnough = False
    
    index = 0
    for busCount in range(1, n + 1):
        limit = (busCount - 1) * t + start
        humanCount = 0 
        while index < length and timetable[index] <= limit:
            humanCount += 1
            index += 1
            if humanCount >= m:
                break
        if index >= length and humanCount < m:
            isEnough = True
            break

        
    if isEnough:
        return sec_to_time(start + (n - 1) * t)
    
    return sec_to_time(timetable[index - 1] - 1)
        
        
    