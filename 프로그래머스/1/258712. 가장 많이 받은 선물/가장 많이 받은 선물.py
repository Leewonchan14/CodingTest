"""
둘중 많이 받은 사람 -> 적게 준사람
선물 지수 == 준거 - 받은거
선물 지수가 낮은 사람 -> 높은 사람에게 준다.
선물지수가 같다면 거래 x
"""

import itertools


def solution(friends, gifts):
    give = {}
    get = {}
    for s in gifts:
        a, b = s.split()
        give[a] = give.get(a, {})
        give[a][b] = give[a].get(b, 0) + 1

        get[b] = get.get(b, {})
        get[b][a] = get[b].get(a, 0) + 1

    jisu = {}

    for a in friends:
        give_thing = sum([i[1] for i in give.get(a, {}).items()])
        get_thing = sum([i[1] for i in get.get(a, {}).items()])
        jisu[a] = give_thing - get_thing

    next_give_count = {}

    combinations = itertools.combinations(friends, 2)
    for a, b in combinations:
        give_a_to_b = give.get(a, {}).get(b, 0)
        give_b_to_a = give.get(b, {}).get(a, 0)
        # 선물 준 기록다르다면
        if give_a_to_b != give_b_to_a:
            # a가 더 적게 줬다면 a가 줘야함
            if give_a_to_b < give_b_to_a:
                next_give_count[b] = next_give_count.get(b, 0) + 1
            # b가 더 적게 줬다면 b가 줘야함
            else:
                next_give_count[a] = next_give_count.get(a, 0) + 1

        # 선물 준 기록이 같다면
        else:
            # 지수가 다르다면
            if jisu[a] != jisu[b]:
                # 지수가 a 가 낮다면 a가 b에게 준다.
                if jisu[a] < jisu[b]:
                    next_give_count[b] = next_give_count.get(b, 0) + 1
                # 지수가 b 가 낮다면 b가 a에게 준다.
                else:
                    next_give_count[a] = next_give_count.get(a, 0) + 1

            # 지수가 같다면 넘어간다.
    gift_count_ls = [i[1] for i in next_give_count.items()]
    return max(gift_count_ls) if gift_count_ls else 0


