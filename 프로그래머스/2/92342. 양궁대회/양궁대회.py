import itertools

def solution(n, info):
    wins = []

    # 2 ** 10 의 경우의 수
    for i in itertools.product((True, False), repeat=11):
        # i = [True, False, ...] 11원소
        # True는 라이언이 이긴 점수

        # info[idx] + 1 == 라이언이 10 - idx점수에 얻기 위해 사용한 화살 갯수
        # 10 - idx == 점수
        arrow_score = [(info[idx] + 1, 10 - idx) for idx,value in enumerate(i) if value]

        # 먼저 주어진 경우로 이길수 있는지 확인

        # 화살갯수가 주어진것보다 많으면 continue
        if sum([x[0] for x in arrow_score]) > n:
            continue

        # 라이언의 점수가 같거나 낮다면 continue
        lion_score = sum([x[1] for x in arrow_score])
        apeach_score = sum([10 - idx for idx, arrow in enumerate(info) if arrow > 0 and not i[idx]])
        if lion_score <= apeach_score:
            continue

        # 점수 차이와 lion의 arrow_score 를 append
        gap = lion_score - apeach_score
        
        arrow = [info[idx] + 1 if value else 0 for idx,value in enumerate(i)]
        # 마지막 0점에 몰아 쏘기
        arrow[-1] = n - sum(arrow)
        
        arrow_mul_score = sum([arrow*score for arrow, score in arrow_score])

        wins.append((gap,1/arrow_mul_score,arrow))

    wins.sort(reverse=True)

    if len(wins) == 0:
        return [-1]
    
    return wins[0][2]
    
    
        