# time to hour:minute
def tth(time: int):
    return time // 60, time % 60


# hour:minute to time
def htt(hour: tuple):
    return hour[0] * 60 + hour[1]


def solution(plans):
    stk = []
    ret = []
    pre_time = 0
    plans.sort(key=lambda x: (x[1]))
    for i in plans:
        subject, start, playtime = i
        playtime = int(playtime)
        now_start_hour, now_start_minute = map(int, start.split(":"))

        now_work = {
            "subject": subject,
            "start": (now_start_hour, now_start_minute),
            "playtime": playtime
        }

        # 잠시 진행 과제에 넣어주기
        if len(stk) == 0:
            stk.append(now_work)
            pre_time = now_work["start"]
            continue

        # 흐른 시간
        flow_time = htt(now_work["start"]) - htt(pre_time)
        pre_time = now_work["start"]

        # 흐른 시간안에 과제들 몽땅 해치우기
        while len(stk) > 0 and flow_time >= stk[-1]["playtime"]:
            pop = stk.pop()
            flow_time -= pop["playtime"]
            ret.append(pop["subject"])

        # 남은 flow_time 처리하기
        if len(stk) > 0:
            stk[-1]["playtime"] -= flow_time

        # 밀린 과제 끝났다면 지금 과제 넣어 주기
        stk.append(now_work)

    # 나머지 stk 내용 마무리 하기
    while len(stk) != 0:
        ret.append(stk.pop()["subject"])

    return ret
