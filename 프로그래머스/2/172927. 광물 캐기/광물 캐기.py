mapper = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]


def getFiro(pick, mineral):
    x = ["diamond", "iron", "stone"].index(mineral)
    return mapper[pick][x]


def split(minerals):
    result = []
    for i in range(0, len(minerals), 5):
        result.append(minerals[i : i + 5])
    return result


def getPick(picks):
    for i in range(3):
        if picks[i] > 0:
            picks[i] -= 1
            return i


def solution(picks, minerals):
    minerals = split(minerals)[: sum(picks)]
    minerals.sort(key=lambda x: sum([getFiro(2, v) for v in x]), reverse=True)

    sumv = 0
    for m in minerals:
        p = getPick(picks)
        sumv += sum([getFiro(p, mm) for mm in m])

    return sumv
